var svg = d3.select("svg");

var projection = d3.geoMercator().center([126.9895, 37.5651]).scale(60000);

var path = d3.geoPath().projection(projection);

d3.json("seoul.geojson", function(error, data) {
    svg.selectAll("path")
        .data(data.features)
        .enter().append("path")
        .attr("d", path)
        .on("click", function(d) {
            alert(d.properties.name + " 클릭됨");
        });
});