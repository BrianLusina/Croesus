/**
 * @author lusinabrian on 06/05/17.
 * @Notes: Returns the store instance
 * It can  also take initialState argument when provided
 * Initialize your SagaMiddleWare.
 * Pass rootReducer and sagaMiddleware to the createStore function to create our redux store.
 * Finally, we run our sagas. You can either spread them or wire them up to a rootSaga.
 */
import { createStore, applyMiddleware } from 'redux';
import rootReducer from '../reducers/rootReducer';
import LogRocket from 'logrocket';
import { composeWithDevTools } from 'redux-devtools-extension';

const configureStore = () => {
    return createStore(
        rootReducer, composeWithDevTools(
            applyMiddleware(LogRocket.reduxMiddleware())
        )
    );
};

export default configureStore;
