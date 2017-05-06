/**
 * @author lusinabrian on 06/05/17.
 * @Notes:
 * This is the root saga that will export our watch saga as a single generator
 * as our root saga
 * Uses fork as an effect creator that provisions the middleware to run a non-blocking call
 * on watchSearchMedia saga.
 * Here, we can bundle our watcher sagas as an array and yield them at once if we have more than one.
 */
