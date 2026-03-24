<?php

namespace Database\Seeders\RolePermissions;

use Illuminate\Database\Seeder;
use Spatie\Permission\Models\Permission;
use Spatie\Permission\Models\Role;

class MunicipalitySuperAdminSeeder extends Seeder
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
                'name' => 'Municipality - Super Admin',
            ]
        ];
        foreach ($roles as $role){
            $createdRole = Role::updateOrCreate($role);
            switch ($createdRole->name){
                case 'Municipality - Super Admin':
                    $createdRole->givePermissionTo(Permission::all());
                break;
            }
        }
    }
}
