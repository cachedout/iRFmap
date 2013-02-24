window.onload=function() {


    runners_cache = null;
    update_lock = null;

    api_root = "http://localhost:8000/api/v1/"

    function main(){
        console.debug("In main()");
//        poll_leaderboard();
//        var poll_timer = setInterval(poll_leaderboard, 2000);
//        update_lock = false;
        get_race();
    }


    function poll_leaderboard(){

        if(update_lock == true) {
            return;
        }

        $.get('http://localhost:8000/poll_leaderboard/1', function (runners) {
            if(! runners_cache) { // Populate on initial page load
                runners_cache = runners;
                $.each(runners, function() {
                    $("#leader_list").append("<li data-id=" + "\"" + this.first_name + "\">" + (this.first_name) + "</li>" );
                });
            }

            if (! _.isEqual(runners, runners_cache)) {
                update_lock = false;
                $("#hidden_leader_list").empty();
                $.each(runners, function() {
                    $("#hidden_leader_list").append("<li data-id=" + "\"" + this.first_name + "\">"  + (this.first_name) + "</li>");
                });
                // Fire Quicksand
                $('#leader_list').quicksand( $('#hidden_leader_list li'), function () {
                    update_lock = false;
                    runners_cache = runners;
                });

            }

        });

    }




    function get_race() {

        var RaceModel = Backbone.Model.extend({
            urlRoot: api_root + 'race/1/?format=json',

        });

        var RaceView = Backbone.View.extend({
            template: _.template('<h1>a template</h1><h2>desc: <%= year %></h2>'),
            initialize: function() {
                thisView = this;
                this.model = new RaceModel();
                this.model.fetch(
                    {
                        success: function() {
                            thisView.render()
                        }
                   }
                );
            },
            render: function() {
                console.debug(this.model.toJSON());
                this.$el.html(this.template(this.model.toJSON()));
                return this;
            }
        });


        var race_view = new RaceView({ el: $("#backbone_test") });


    }



    main();

}