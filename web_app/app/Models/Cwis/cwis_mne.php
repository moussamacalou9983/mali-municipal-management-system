<?php

namespace App\Models\Cwis;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class cwis_mne extends Model
{
    protected $table = 'cwis.data_cwis';
  
        protected $fillable = [    
        'year',
       ];
}
