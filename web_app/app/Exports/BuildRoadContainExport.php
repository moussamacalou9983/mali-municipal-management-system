<?php

namespace App\Exports;

namespace App\Exports;

use Illuminate\Contracts\View\View;
use Maatwebsite\Excel\Concerns\FromView;
use DB;
use Maatwebsite\Excel\Concerns\WithTitle;
use Maatwebsite\Excel\Concerns\WithEvents;


class BuildRoadContainExport  implements FromView, WithTitle, WithEvents

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
    $containmentQuery = "
    SELECT DISTINCT ON (final_result.bin) final_result.*
    FROM (
        SELECT bc.bin, bc.containment_id
        FROM building_info.build_contains bc
        JOIN building_info.buildings b
          ON bc.bin = b.bin
        WHERE b.deleted_at IS NULL
          AND bc.bin IS NOT NULL
          AND bc.containment_id IS NOT NULL
          AND b.road_code IN (" . implode(',', $roadCodes) . ")
          AND bc.deleted_at IS NULL
    ) final_result
    ORDER BY final_result.bin ASC";

    $buildingResults = DB::select($containmentQuery);

    return view('exports.build-contain', compact('buildingResults'));
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
        return 'Build Contain List';
    }
}
