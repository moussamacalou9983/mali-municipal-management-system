<?php

namespace App\Exports;

use Illuminate\Contracts\View\View;
use Maatwebsite\Excel\Concerns\FromView;
use DB;
use Maatwebsite\Excel\Concerns\WithTitle;
use Maatwebsite\Excel\Concerns\WithEvents;

class ContainmentsRoadListExport implements FromView, WithTitle, WithEvents
{
    private $codes;
    
      /**
     * BuildingsExport constructor.
     *
     * @param $codes
     */
    public function __construct($codes)
    {
        $this->codes = $codes;
    }

      /**
     * Generates the view for exporting.
     *
     * @return View
     */
    public function view(): View
    {
    $roadCodesStr = $this->codes;
    
    $roadCodes = explode (",", $roadCodesStr); 
    $roadCodes = array_map(function($value) { return "'" . $value . "'"; }, $roadCodes);
 

    // Construct SQL query to select containments associated with the buildings
    $containmentQuery = "SELECT DISTINCT ON (final_result.id) final_result.*
        FROM (
            SELECT 
                c.*, 
                ct.type AS containment_type, 
                b.bin AS bin
            FROM fsm.containments c
            LEFT JOIN building_info.build_contains bc 
                ON bc.containment_id = c.id 
                AND bc.deleted_at IS NULL 
                AND bc.bin IS NOT NULL 
                AND bc.containment_id IS NOT NULL
            LEFT JOIN building_info.buildings b 
                ON b.bin = bc.bin 
                AND b.deleted_at IS NULL
            LEFT JOIN fsm.containment_types ct 
                ON ct.id = c.type_id
            WHERE 
            b.road_code IN (" . implode(',', $roadCodes) . ")
            AND 
            c.deleted_at IS NULL
        ) final_result
        ORDER BY final_result.id";

        $containmentResults = DB::select($containmentQuery);
    
        return view('exports.containments-list', compact('containmentResults'));
    }

     /**
     * Registers events for the export.
     *
     * @return array
     */
    public function registerEvents(): array
    {
        return [
            AfterSheet::class => function (AfterSheet $event) {
                $event->sheet->getStyle('A1:B1')->applyFromArray([
                    'font' => [
                        'bold' => true
                    ]
                ]);
            }
        ];
    }

     /**
     * @return string
     */
    public function title(): string
    {
        return 'Containment List';
    }
}