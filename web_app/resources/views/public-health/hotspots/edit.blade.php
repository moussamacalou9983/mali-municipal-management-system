@extends('layouts.dashboard')
@section('title', $page_title)
@section('content')
@include('layouts.components.error-list')
@include('layouts.components.success-alert')
@include('layouts.components.error-alert')
<div class="card card-info">
	{!! Form::model($Hotspots, ['method' => 'PATCH', 'action' => ['PublicHealth\HotspotController@update', $Hotspots], 'class' => 'form-horizontal']) !!}
		@include('public-health/hotspots.partial-form', ['submitButtomText' => 'Update'])
	{!! Form::close() !!}
</><!-- /.card -->
@stop