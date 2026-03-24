window._ = require('lodash');

try {
    window.$ = window.jQuery = require('jquery');
    window.Popper = require('popper.js').default;
    require('bootstrap');

    // AdminLTE code here.
    require('admin-lte');
    require('bootstrap-datepicker');
    window.moment = require('moment');
    require('daterangepicker');
    require('select2');
    require('chart.js');



} catch (e) {
    console.log(e);
}


/**
 * Echo exposes an expressive API for subscribing to channels and listening
 * for events that are broadcast by Laravel. Echo and event broadcasting
 * allows your team to easily build robust real-time web applications.
 */

// import Echo from 'laravel-echo';

// window.Pusher = require('pusher-js');

// window.Echo = new Echo({
//     broadcaster: 'pusher',
//     key: process.env.MIX_PUSHER_APP_KEY,
//     cluster: process.env.MIX_PUSHER_APP_CLUSTER,
//     forceTLS: true
// });