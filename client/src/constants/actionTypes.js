/**
 * @author lusinabrian on 06/05/17.
 * @Notes:
 * Action creators are functions that return plain Javascript object of action type and an
 * optional payload. So action creators create actions that are dispatched to the store.
 * They are just pure functions. defines our action types in a file and export them for ease
 * of use in other files. They’re constants and it’s a good practice to define them in a
 * separate file(s).
 */
export const LOGIN_USER_SUCCESS = 'LOGIN_USER_SUCCESS';
export const LOGIN_USER_FAILURE = 'LOGIN_USER_FAILURE';
export const LOGIN_USER_REQUEST = 'LOGIN_USER_REQUEST';
export const LOGOUT_USER = 'LOGOUT_USER';

export const REGISTER_USER_SUCCESS = 'REGISTER_USER_SUCCESS';
export const REGISTER_USER_FAILURE = 'REGISTER_USER_FAILURE';
export const REGISTER_USER_REQUEST = 'REGISTER_USER_REQUEST';

export const FETCH_PROTECTED_DATA_REQUEST = 'FETCH_PROTECTED_DATA_REQUEST';
export const RECEIVE_PROTECTED_DATA = 'RECEIVE_PROTECTED_DATA';

export const SELECTED_IMAGE = 'SELECTED_IMAGE';
export const FLICKR_IMAGES_SUCCESS = 'FLICKR_IMAGES_SUCCESS';
export const SELECTED_VIDEO = 'SELECTED_VIDEO';
export const SHUTTER_VIDEOS_SUCCESS = 'SHUTTER_VIDEOS_SUCCESS';
export const SEARCH_MEDIA_REQUEST = 'SEARCH_MEDIA_REQUEST';
export const SEARCH_MEDIA_SUCCESS = 'SEARCH_MEDIA_SUCCESS';
export const SEARCH_MEDIA_FAILURE = 'SEARCH_MEDIA_FAILURE';

export const REQUEST_BLOG_POST = 'REQUEST_BLOG_POST';
export const REQUEST_BLOG_POST_SUCCESS = 'REQUEST_BLOG_POST_SUCCESS';
export const REQUEST_BLOG_POST_ERROR = 'REQUEST_BLOG_POST_ERROR';

export const ADD_BLOG = 'ADD_BLOG';
export const ADD_BLOG_SUCCESS = 'ADD_BLOG_SUCCESS';
export const ADD_BLOG_ERROR = 'ADD_BLOG_ERROR';

export const DELETE_BLOG = 'DELETE_BLOG';
export const DELETE_BLOG_SUCCESS = 'DELETE_BLOG_SUCCESS';
export const DELETE_BLOG_ERROR = 'DELETE_BLOG_ERROR';