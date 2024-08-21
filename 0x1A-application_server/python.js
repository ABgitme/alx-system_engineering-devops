// Execuite when DOM is loaded
$(document).ready(init);
// host URL for API requests
const HOST = "34.239.253.220";
//initialization functions
function init() {
  // obj to store selected amenities
  const amenityObj = {};

  //checkbox listening inside ".amenities .popover
  $(".amenities .popover input").change(function() {
    //if the checkbox checked then add its data id and data name
    if ($(this).is(":checked")) {
      amenityObj[$(this).attr("data-name")] = $(this).attr("data-id");
    } else if ($(this).is(":not (:checked)")) {
      // if not checked then delete data-name from amenityObj
      delete amenityObj[$(this).attr("data-name")];
    }

    const names = Object.keys(amenityObj);
    $(".amenities h4").text(names.sort().join(", "));
  });

  apiStatus();
}

// fuction to check api status
function apiStatus() {
  //api endpoint URL
  const API_URL = `http://${HOST}:5001/api/v1/status/`;
  //send GET request to get its status
  $.get(API_URL, (data, textStatus) => {
    if (textStatus === "success" && data.status === "OK") {
      $("#api_status").addClass("available");
    } else {
      $("#api_status").removeClass("available");
    }
  });
}
