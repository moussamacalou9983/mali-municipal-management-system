<?php

namespace Database\Seeders\BuildingInfo;

use Illuminate\Database\Seeder;
use App\Models\BuildingInfo\WaterSource;
use DB;

class WaterSourceSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $types =  array(
            [1, 'Municipal/Public water supply'],
            [2, 'Deep boring'],
            [3, 'Tube well'],
            [4, 'Dug well'],
            [5, 'Private Tanker water'],
            [6, 'Jar Water'],
            [7, 'Spring/River/Canal'],
            [8, 'Stone spout/Pond'],
            [9, 'Rainwater'],
            [10,'Others']

        );

     foreach ($types as $type) {

        $existWaterSource =  WaterSource::where('id', $type[0])->first();
        if($existWaterSource)
        {

        }
        else
        {
            $existWaterSource = new WaterSource;
            $existWaterSource->id = $type[0];
        }
        $existWaterSource->source = $type[1];
        $existWaterSource->save();
    }
    }
}



