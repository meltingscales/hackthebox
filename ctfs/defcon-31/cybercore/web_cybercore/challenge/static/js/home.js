function randomNumber(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}


$(document).ready(function () {

    for (i = 0; i <= 100; i++) {
        $("#stars").append("<div class='star'></div>");
    }

    var width = 600,
        height = 500,
        sens = 0.25,
        focused;

    //Setting projection

    var projection = d3.geo.orthographic()
        .scale(245)
        .rotate([0, 0])
        .translate([width / 2, height / 2])
        .clipAngle(90);

    var path = d3.geo.path()
        .projection(projection);

    //SVG container

    var svg = d3.select("#globe").append("svg")
        //.attr("width", width)
        //.attr("height", height)
        .attr("viewBox", "0 0 " + width + " " + height);

    //Adding water

    svg.append("path")
        .datum({ type: "Sphere" })
        .attr("class", "water")
        .attr("d", path);

    var countryTooltip = d3.select("#atlas-menu").append("div").attr("class", "countryTooltip"),
        countryList = d3.select("#atlas-menu").append("select").attr("name", "countries");


    queue()
        .defer(d3.json, "https://gist.githubusercontent.com/djdmsr/119dca130259fbf5a39469bb1bc40c85/raw/43ff28626319a187e94c8add1b16c5f16c21f92d/world-110m.v1.json")
        .defer(d3.tsv, "https://gist.githubusercontent.com/djdmsr/5be8853ee63dc2864ac0c14349092214/raw/f19ae25092abbd67cd0e84882d9c7fb9b0324132/world-110m-country-names-light.tsv")
        .await(ready);

    //Main function

    function ready(error, world, countryData) {

        var countryById = {},
            countries = topojson.feature(world, world.objects.countries).features;

        //Adding countries to select

        countryData.forEach(function (d) {
            countryById[d.id] = d.name;
            option = countryList.append("option");
            option.text(d.name);
            option.property("value", d.id);
        });

        //Drawing countries on the globe

        var world = svg.selectAll("path.land")
            .data(countries)
            .enter().append("path")
            .attr("class", "land")
            .attr("d", path)

            //Drag event

            .call(d3.behavior.drag()
                .origin(function () { var r = projection.rotate(); return { x: r[0] / sens, y: -r[1] / sens }; })
                .on("drag", function () {
                    var rotate = projection.rotate();
                    projection.rotate([d3.event.x * sens, -d3.event.y * sens, rotate[2]]);
                    svg.selectAll("path.land").attr("d", path);
                    svg.selectAll(".focused").classed("focused", focused = false);
                }))

            //Mouse events

            .on("mouseover", function (d) {
                countryTooltip.text(countryById[d.id])
                    .style("left", (d3.event.pageX + 7) + "px")
                    .style("top", (d3.event.pageY - 15) + "px")
                    .style("display", "block")
                    .style("opacity", 1);
            })
            .on("mouseout", function (d) {
                countryTooltip.style("opacity", 0)
                    .style("display", "none");
            })
            .on("mousemove", function (d) {
                countryTooltip.style("left", (d3.event.pageX + 7) + "px")
                    .style("top", (d3.event.pageY - 15) + "px");
            });

        //Country focus on option select

        d3.select("select").on("change", function () {
            var rotate = projection.rotate(),
                focusedCountry = country(countries, this),
                p = d3.geo.centroid(focusedCountry);

            svg.selectAll(".focused").classed("focused", focused = false);

            //Globe rotating

            (function transition() {
                d3.transition()
                    .duration(2500)
                    .tween("rotate", function () {
                        var r = d3.interpolate(projection.rotate(), [-p[0], -p[1]]);
                        return function (t) {
                            projection.rotate(r(t));
                            svg.selectAll("path").attr("d", path)
                                .classed("focused", function (d, i) { return d.id == focusedCountry.id ? focused = d : false; });
                        };
                    })
            })();
        });

        function country(cnt, sel) {
            for (var i = 0, l = cnt.length; i < l; i++) {
                if (cnt[i].id == sel.value) { return cnt[i]; }
            }
        };

    };

    opt = document.querySelector('select');
    opt.addEventListener('change', (event) => {
        let total_bots = randomNumber(10000, 99999)
        let hib = randomNumber(100, 999)
        let act = randomNumber(1000, 9999)

        $('#ttr').text(total_bots);
        $('#ta').text(hib);
        $('#tat').text(act);

        $('#sarea').text($("#atlas-menu :selected").text());
    });

});

setTimeout(() => {
    at = document.querySelector('select');
    at.options[0].selected = true;

    var event = new Event('change');

    at.dispatchEvent(event);
}, 1000)