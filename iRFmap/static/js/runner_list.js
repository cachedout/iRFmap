window.onload=function() {


    function main(){
        console.debug("In main()");
        poll_leaderboard()
    }


    function poll_leaderboard(){
        $.get('http://localhost:8000/poll_leaderboard/1', function (leaderboard) {
            $.each(leaderboard, function(runner) { 
                $("#leader_list").append("<li>" + (leaderboard[runner].first_name) + "</li>" );
            }); 
        });

    }


    main();

}