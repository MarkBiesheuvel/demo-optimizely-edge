// Optimizely Account ID
var ACCOUNT_ID = '21537940595';

// Regular expression to match incoming URI
var URI_REGEX = new RegExp('/optimizely-edge/(.+)\.js')

// Format of outgoing URI
var URI_FORMAT = `/edge-client/v1/${ACCOUNT_ID}/$1`

function handler(event) {
    // Collect request object from CloudFront event
    var request = event.request;

    // Verify URI pattern
    if (!request.uri.match(URI_REGEX)) {
      throw `Invalid URI: ${request.uri}`
    }

    // Transform the URI into the correct pattern
    request.uri = request.uri.replace(URI_REGEX, URI_FORMAT);

    // Return modified request object
    return request;
}