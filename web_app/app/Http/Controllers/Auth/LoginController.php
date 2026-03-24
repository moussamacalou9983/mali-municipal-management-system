<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Http\Requests\LoginRequest;
use Illuminate\Support\Facades\Auth;


class LoginController extends Controller
{


    /**
     * Display login page.
     * 
     * @return Renderable
     */
    public function show()
    {
        
        return  redirect('/');
    }

    /**
     * Handle account login request
     * 
     * @param LoginRequest $request
     * 
     * @return \Illuminate\Http\Response
     */
    public function login(LoginRequest $request)
    {
        $credentials = $request->getCredentials();
        
        if (!Auth::validate($credentials)) {
            return redirect()->back()
                ->withErrors(trans('auth.failed'));
        }
    
        $user = Auth::getProvider()->retrieveByCredentials($credentials);
    
        // Check for not allowed roles
        $notallowedRoles = [
            'Municipality - Building Surveyor',
            'Service Provider - Emptying Operator',
            'Municipality - Building Surveyor (Ward)'
        ];
    
        if ($user->roles()->whereIn('name', $notallowedRoles)->exists()) {
            Auth::logout();
            return redirect()->back()
                ->withErrors(['login' => 'You are not allowed to log in with your current role.']);
        }
    
        Auth::login($user, $request->get('remember'));
    
        return $this->authenticated($request, $user);
    }
    

    /**
     * Handle response after user authenticated
     * 
     * @param Request $request
     * @param Auth $user
     * 
     * @return \Illuminate\Http\Response
     */
    protected function authenticated(Request $request, $user) 
    {
        return redirect('/');
    }
}