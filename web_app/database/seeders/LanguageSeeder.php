<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Carbon\Carbon;

class LanguageSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $timestamp = Carbon::now();

        DB::table('language.languages')->updateOrInsert(
            ['code' => 'fr'],
            [
                'name' => 'Francais',
                'status' => true,
                'created_at' => $timestamp,
                'updated_at' => $timestamp,
                'deleted_at' => null,
            ]
        );

        DB::table('language.languages')->updateOrInsert(
            ['code' => 'en'],
            [
                'name' => 'English',
                'status' => true,
                'created_at' => $timestamp,
                'updated_at' => $timestamp,
                'deleted_at' => null,
            ]
        );
    }
}
