function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

//function to check whether a name exists in an array
function containsObject(obj, list) {
    for (var i = 0; i < list.length; i++) {
        if (list[i] === obj) {
            return true;
        }
    }

    return false;
}

function performAction() {
    var csrftoken = getCookie('csrftoken');
    var action = $(document.getElementById("actions")).val();
    console.log("Selected action-"+action);

    var status_options = ["NEW", "Back Filling", "Investigating", "Resolved", "Shipped", "Wont Fix", "False Alarm", "Ignore", "Not Tracking", "Too Low"];

    //get ids of all the checked alerts
   var checkedIds = $(":checkbox:checked").map(function() {
        return this.id;
    }).get();
   //Check if atleast one alert is chosen
   if (checkedIds.length<=0 && action != "Actions") {
    console.log("No alert chosen");
    alert("Please Choose atleast one Alert");
   } else {
        var ids = {};
        for (var alertid in checkedIds) {
            if (!checkedIds[alertid].split('-')[2])
                continue;

            ids[alertid] = checkedIds[alertid].split('-')[2];
        }
        checkedIds = ids;
        var alertids = $.map(checkedIds, function(value, index) {
                    return [value];
                }).join(",");
        console.log(alertids);
        //Check if status has to be changed
        if (containsObject(action, status_options)) {
            console.log("change status-"+action);
            $.ajax({
                 url: "/updatefields?type=status",
                type: "POST",
                data: {
                    id: alertids,
                    status: action
                },
                success: console.log("DONE CHANGING STATUS")
            });
        } else if (action == "Change Revision") {
            var newRev = prompt("Please enter new Revision");    
            if (newRev != null) {
                console.log('new revision-'+newRev);
                $.ajax({
                    url: "/updatefields?type=revision",
                    type: "POST",
                    data: {
                        id: alertids,
                        revision: newRev,
                    },
                    success: console.log("DONE CHANGING REVISION")
                });
            }
        } else if (action == "Add Bug") {
            var BugID = prompt("Please enter Bug ID");
            console.log('BUG ID-'+BugID);
            if (BugID != null) {
                $.ajax({
                     url: "/updatefields?type=bug",
                    type: "POST",
                    data: {
                        id: alertids,
                        BugID: BugID
                    },
                    success: console.log("DONE ADDING BUG")
                });
            }
        }

        else if (action == "Add Comment") {
            $(function() {
                $("#addCommentpopup").dialog({
                    autoOpen: false,
                    modal: true,
                    position: { my: 'top', at: 'top+150' },
                    buttons: { 
                        Ok: function() {
                            var email = $("#commentName").val();
                            var comment = $("#commentText").val();
                            console.log(email+"---"+comment);
                            $.ajax({
                                     url: "/updatefields?type=comment",
                                    type: "POST",
                                    data:{
                                        id: alertids,
                                        comment: comment,
                                        email: email,
                                    }
                            });

                            $(this).dialog("close");
                       },
                        Cancel: function () {
                            $(this).dialog("close");
                        }
                    }
                });
            });
            $("#addCommentpopup").dialog("open");
        } else if (action == "Change Branch") {
            $(function() {
                $("#changeBranchpopup").dialog({
                    autoOpen: false,
                    modal: true,
                    position: { my: 'top', at: 'top+150' },
                    buttons: { 
                        Ok: function() {
                            var branch = $("#branchName").val();
                            var rev = $("#revisionName").val();
                            console.log(branch+"---"+rev);
                            $.ajax({
                                    url: "/updatefields?type=branch",
                                    type: "POST",
                                    data:{
                                        id: alertids,
                                        branch: branch,
                                        revision: rev,
                                    }
                            });
                            $(this).dialog("close");
                       },
                        Cancel: function () {
                            $(this).dialog("close");
                        }
                    }
                });
            });
            $("#changeBranchpopup").dialog("open");
        } else if (action == 'Duplicate') {
            $(function() {
                $("#markDuplicatepopup").dialog({
                    autoOpen: false,
                    modal: true,
                    position: { my: 'top', at: 'top+150' },
                    buttons: { 
                        Ok: function() {
                            var new_rev = $("#markDuplicateRev").val();
                            console.log(new_rev);
                            $.ajax({
                                    url: "/updatefields?type=duplicate",
                                    type: "POST",
                                    data:{
                                        id: alertids,
                                        rev: new_rev,
                                    }
                            });
                            
                            $(this).dialog("close");
                       },
                        Cancel: function () {
                            $(this).dialog("close");
                        }
                    }
                });
            });
            $("#markDuplicatepopup").dialog("open");
        } else if (action == 'Backout') {
            $(function() {
                $("#BackoutPopup").dialog({
                    autoOpen: false,
                    modal: true,
                    position: { my: 'top', at: 'top+150' },
                    buttons: { 
                        Ok: function() {
                            var bug = $("#BackoutPopupText").val();
                            console.log(bug);
                            $.ajax({
                                     url: "/updatefields?type=backout",
                                    type: "POST",
                                    data:{
                                        id: alertids,
                                        bug: bug
                                    }
                            });
                            $(this).dialog("close");
                       },
                        Cancel: function () {
                            $(this).dialog("close");
                        }
                    }
                });
            });
            $("#BackoutPopup").dialog("open");
        }      
   }
}