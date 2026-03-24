<?php
// Last Modified Date: 18-04-2024
// Developed By: Innovative Solution Pvt. Ltd. (ISPL)  (© ISPL, 2022)
namespace App\Models\Fsm;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class EmptyingService extends Model
{
    use SoftDeletes;
    protected $table = 'fsm.emptying_services';
    protected $primaryKey = 'id';

    public function containment()
    {
        $this->belongsTo('App\Models\Fsm\Containment', 'contain');
    }

    public function serviceProvider()
    {
        $this->belongsTo('App\Models\Fsm\ServiceProvider', 'service_provider_code');
    }

    public function user()
    {
        return $this->belongsTo('App\User');
    }
}
