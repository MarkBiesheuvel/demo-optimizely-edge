// Optimizely Account ID
var ACCOUNT_ID = '21537940595';

// Performance Edge Project ID
var PROJECT_ID = '21967710833';

function handler(event) {
    // Collect information from CloudFront event
    var request = event.request;

    // Hardcode the URI, as CloudFront will try to append current path
    request.uri = `/edge-client/v1/${ACCOUNT_ID}/${PROJECT_ID}`;

    // Return modified request object
    return request;
}