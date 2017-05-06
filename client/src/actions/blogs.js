/**
 * @author lusinabrian on 06/05/17.
 * @Notes:
 */
import * as actionTypes from '../constants/actionTypes';
import { get, post, del } from '../api/api';

export function requestBlogs() {
    return async dispatch => {
        dispatch({
            type: actionTypes.REQUEST_KITTENS
        });

        try {
            const result = await get('http://0.0.0.0:5000/json');
            console.log(result);

            dispatch({
                type: actionTypes.REQUEST_KITTENS_SUCCESS,
                kittens: result
            });
        } catch(e) {
/*            dispatch({
                type: actionTypes.REQUEST_KITTENS_ERROR
            });*/
        }
    }
}
