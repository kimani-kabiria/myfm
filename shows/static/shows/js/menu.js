document.write("
<div class="left-side sticky-left-side">
    <div class="logo">
        <h1><a href="index.html">my<span>FM</span></a></h1>\
    </div>\
    <div class="logo-icon text-center">
        <a href="index.html"><img src="{% static 'shows/images/icon.png' %}" style="width: 30px; height: 30px"></a>\
    </div>\
    <div class="left-side-inner">
            <ul class="nav nav-pills nav-stacked custom-nav">
                <li class="menu-list"><a href="/shows/"><i class="lnr lnr-indent-increase"></i> <span>Shows</span></a>\
                <li><a href="#"><i class="camera"></i> <span>Stations</span></a></li>\
                <li><a href="#" data-toggle="modal" data-target="#myModal1"><i class="fa fa-th"></i><span>Apps</span></a></li>\
            </ul>\
    </div>\
    <div class="modal fade" id="myModal1" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog facebook" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\
                </div>\
                <div class="modal-body">
                    <div class="app-grids">
                        <div class="app">
                        <div class="col-md-5 app-left mpl">
                            <h3>Mosaic mobile app on your smartphone!</h3>\
                            <p>Download and Avail Special Songs Videos and Audios.</p>\
                            <div class="app-devices">
                                <h5>Gets the app from</h5>\
                                <a href="#"><img src="{% static 'shows/images/1.png' %}" alt=""></a>\
                                <a href="#"><img src="{% static 'shows/images/2.png' %}" alt=""></a>\
                                <div class="clearfix"> </div>\
                            </div>\
                        </div>\
                        <div class="col-md-7 app-image">
                            <img src="{% static 'shows/images/apps.png' %}" alt="">\
                        </div>\
                        <div class="clearfix"></div>\
                        </div>\
                    </div>\
                </div>\
            </div>\
        </div>\
    </div>\
</div>\
");