@php
    $websiteUrl = config('branding.public_website_url');
    $githubUrl = config('branding.public_github_url');
    $youtubeUrl = config('branding.public_youtube_url');
    $primaryUrl = $websiteUrl ?: $githubUrl;
@endphp

<div class="float-right d-none d-sm-inline">
    <strong>Personnalisation :</strong>
    @if ($primaryUrl)
        <a href="{{ $primaryUrl }}" target="_blank" rel="noopener">{{ config('branding.organization_name') }}</a>
    @else
        <span>{{ config('branding.organization_name') }}</span>
    @endif
    @if ($githubUrl)
        | <a href="{{ $githubUrl }}" target="_blank" rel="noopener">GitHub</a>
    @endif
    @if ($youtubeUrl)
        | <a href="{{ $youtubeUrl }}" target="_blank" rel="noopener">YouTube</a>
    @endif
</div>

<strong>
    Base sur
    <a href="{{ config('branding.original_repository_url') }}" target="_blank" rel="noopener">
        {{ config('branding.original_project_name') }}
    </a>.
    Credits originaux : {{ config('branding.original_creators') }}.
    Licence :
    <a href="{{ config('branding.original_license_url') }}" target="_blank" rel="noopener">
        {{ config('branding.original_license_name') }}
    </a>.
</strong>
