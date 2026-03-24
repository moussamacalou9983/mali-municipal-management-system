<?php

namespace Database\Seeders\RolePermissions;

use Illuminate\Database\Seeder;
use Spatie\Permission\Models\Permission;
use Spatie\Permission\Models\Role;

class MunicipalityBuildingSurveyorSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        app()[\Spatie\Permission\PermissionRegistrar::class]->forgetCachedPermissions();
        $roles = [
            [
                'name' => 'Municipality - Building Surveyor',
            ]
           
        ];
        foreach ($roles as $role){
            $createdRole = Role::updateOrCreate($role);
            switch ($createdRole->name){
                case 'Municipality - Building Surveyor':
                    $createdRole->givePermissionTo(Permission::all()->whereIn('group',['API'])
                    ->where('name','Access Building Survey API'));
                    break;
            }
        }
    }
}
