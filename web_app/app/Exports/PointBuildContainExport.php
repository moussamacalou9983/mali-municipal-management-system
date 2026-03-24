<?php

namespace App\Exports;

use Maatwebsite\Excel\Concerns\FromCollection;
namespace App\Exports;

use Illuminate\Contracts\View\View;
use Maatwebsite\Excel\Concerns\FromView;
use DB;
use Maatwebsite\Excel\Concerns\WithTitle;
use Maatwebsite\Excel\Concerns\WithEvents;
class PointBuildContainExport implements FromView, WithTitle, WithEvents
{
    /**
    * @return \Illuminate\Support\Collection
    */

        private $longitude;
        private $latitude;
        private $distance;
    /**
     * BuildingsExport constructor.
     *
     * @param $longitude
     * @param $latitude
     * @param $distance
     *
     */
    public function __construct($longitude, $latitude, $distance)
    {
        $this->longitude = $longitude;
        $this->latitude = $latitude;
        $this->distance = $distance;
    }

          /**
     * Generates the view for exporting.
     *
     * @return View
     */
    public function view(): View
    {
        if ($this->distance > 0) {
            $distance = $this->distance;
        } else {
            $distance = 0;
        }
        $buildingQuery = "SELECT bc.bin, bc.containment_id
        FROM building_info.build_contains bc 
        JOIN building_info.buildings b ON bc.bin = b.bin AND b.deleted_at IS NULL AND bc.bin IS NOT NULL AND bc.containment_id IS NOT NULL
        WHERE ST_Intersects(
                    ST_Buffer(
                        ST_SetSRID(ST_Point(" . $this->longitude . ", " . $this->latitude . "), 4326)::GEOGRAPHY,
                        " . $distance . "
                    )::GEOMETRY,
                    b.geom
                )
        AND bc.deleted_at IS NULL
        ORDER BY bc.bin ASC";
    
        $buildingResults = DB::select($buildingQuery);
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
        return 'Build-Contain List';
    }
    }
