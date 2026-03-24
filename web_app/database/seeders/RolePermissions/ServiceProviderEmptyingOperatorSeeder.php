<?php

namespace Database\Seeders\RolePermissions;
use Spatie\Permission\Models\Role;
use Illuminate\Database\Seeder;
use Spatie\Permission\Models\Permission;
class ServiceProviderEmptyingOperatorSeeder extends Seeder
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
               'name' => 'Service Provider - Emptying Operator',
            ],
        ];
        foreach ($roles as $role){
            $createdRole = Role::updateOrCreate($role);
            switch ($createdRole->name){
                
                   
                    case 'Service Provider - Emptying Operator':
                        $createdRole->givePermissionTo(Permission::all()->whereIn('group',['API'])
                        ->where('name','Access Emptying Service API'));
                        break;
             
                   
            }
        }
    }
}
