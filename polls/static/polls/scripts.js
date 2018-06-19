function makebuttons(){
    var buttons = [];
    var i=0;
    var teststring1 = ["This","Is","My","Final", "Project", "Category", "New"];
    var teststring = ["THIS", "IS", "MY","FINAL", "PROJECT", "CATEGORY", "NEW"];
    var categoryList = ["cookware", "Knifes", "Grills", "Glass", "Bar", "Containers", "All"];
    var list ="";
    for (i in teststring1){
        list += '<div class="dropelement"><dt><p class="test">' + teststring1[i] + '</p></dt></div>'; 
    } 
    var categories = '';
    '{% for category in categories %}';
        categories += '<a href="{{ category.get_absolute_url }}"><div class="dropelement"><dt><p class="test">{{ category.name }}</p></dt></div></a>';
    '{% endfor %}';
    // buttons.push('<a href=""><form action="{% url ' + "'polls:catalogue'" + '%}" method="get"/><button class="windownext" name="category" value="All"><h6 style="color: #c7c7c7">CATALOGUE</h6><div class="drop"' + categories + '</div></button></form></a>');
    // buttons.push('<a href="http://ide50-stanly-white.cs50.io:8080/polls/categories"><button class="windownext" id="catalogue"><h6 style="color: #0a0043">CATEGORIES</h6></button><a/>');
    buttons.push('<a href="http://ide50-stanly-white.cs50.io:8080/polls/categories"><button class="windownext" id="test"><h6 style="color: #0a0043">CATEGORIES</h6><div class="drop">' + categories + '</div></button><a/>');
    for (i in teststring){
        buttons.push('<a href=""><button class="windownext" id="test"><h6 class="solid"></h6><div class="drop">' + list + '</div></button><a/>');
        $('#post').append(buttons[i]);
    }
    $("h6.solid").append(function(i){
        return teststring[i];
    });
}
$(makebuttons()).appendTo('#post');
            