Netbox Patch for router to router network map 

modify mutils and change api token to match yours 


cp router.png to /opt/netbox/netbox/project-static/img/
cp lnet_d3js.js /opt/netbox/netbox/project-static/js/
cp d3js_v5_utils.js /opt/netbox/netbox/project-static/js/
cp network_map.html /opt/netbox/netbox/templates/extras
cp mutils.py /opt/netbox/netbox/extras/

Apply netbox_patch.diff 
