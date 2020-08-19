//https://data.gov.uk/dataset/daaafdcc-f7c7-41ff-80eb-b0b15efd1414/local-authority-districts-december-2017-generalised-clipped-boundaries-in-united-kingdom-wgs84
//Adapted from https://bl.ocks.org/kierandriscoll/93f75337ee73d89e764378cd2d3cc0dd
//
/*
WORKFLOW FOR IMPORTING MAP SHAPES:
Shape file from UK official sources:
http://sedsh127.sedsh.gov.uk/Atom_data/ScotGov/ZippedShapefiles/SG_NHS_HealthBoards_2019.zip


Load UK local authorities and Scottish health districts into QGIS
Delete districts in Buckinghamsire; cut and paste shape of Bucks
Delete Scottish local authorities; load Scottish health districts
Rename columns (field attributes)  to areaname, areacode (so as to match) - using 'Processing Toolbox - Refactor Fields'
Reduce size of file with simplify - Vector - Geometry Tools - Simplify (applying 0.001 degrees)
Save as GeoJson - with options - add Bounding Box
Import into mapshaper and then save as TopoJson  https://mapshaper.org/  
Put file in graph/static/graph/json/ folder
Adjust shape_url variable in line elow for new file name.
*/
   var display_value='cases_rate'
   var shape_url = "/static/graph/json/UK_corrected_topo.json"
//document.getElementById("shape_location").value;
   var map_data_url="/graph/api_rates"
   
   if (display_value=='cases_rate'){
	var legend0 = -1, legend1 = 5, legend2 = 10, legend3 = 20, legend4 = 40, legend5 = 50; // Must be 6 ranges
   var stat_name = 'Covid-19 cases last 7 days';           // This will be displayed on the map 
   var colour_scheme = 'Blue';                             // Either: 'Purple', 'Red', Blue, 'Green', 'Orange', 'R2G'
	
	
	}
	else{
	var legend0 = 20, legend1 = 40, legend2 = 70, legend3 = 90, legend4 = 110, legend5 = 130; // Must be 6 ranges	
  var stat_name = 'Excess deaths per 100,000 people';     // This will be displayed on the map 
   var colour_scheme = 'Red';                             // Either: 'Purple', 'Red', Blue, 'Green', 'Orange', 'R2G'

	}
   var map;
   var topoLayer;
   var colourmatrix = {
                    R2G:["#cb181d","#fb6a4a","#fcbba1","#c7e9c0","#74c476","#238b45"]
                    ,Green:["#c7e9c0", "#a1d99b", "#74c476", "#41ab5d", "#238b45", "#005a32"]
                    ,Purple: ['#dadaeb','#bcbddc','#9e9ac8','#807dba','#6a51a3','#4a1486']
                    ,Red: ["#fcbba1", "#fc9272", "#fb6a4a", "#ef3b2c", "#cb181d", "#99000d"]
                    ,Blue:["#9ecae1", "#6baed6", "#4292c6", "#2171b5", "#085192", "#08306b"]
                    ,Orange:["#fdd0a2", "#fdae6b", "#fd8d3c", "#f16913", "#d94801", "#8c2d04"]
                    }

//var lagb = "https://raw.githubusercontent.com/kierandriscoll/UK-Topojson/master/Local-Authorities/Local_Auths_Dec16_Gen_Clip_GB.json"
//    var shape_url = "/static/graph/json/Local_Auths_Dec16_Gen_Clip_UK.json"

    var layers = {};
    var references={};
    var startplace="Birmingham";
    var mapLookup;

function loadmap(){
	   

   // Local Authority Boundaries data source
 //  var lagb = '{% static 'graph/json/Local_Auths_Dec16_Gen_Clip_GB.json' %}';
 
   var fmtn = d3.format(",.0f"); // Formats all numbers with commas and 0dp
   var fmtph = d3.format(".1%");  // Formats percentages with % and 1dp (only for hover)
   var fmtpl = d3.format(".0%");  // Formats percentages with % and 0dp (only for legend)
 
   // Define Map area/position and any background tiles
   map = new L.Map('mapid', { center: new L.LatLng(53.10, -1.26),zoom: 7   });
   var layer = new L.StamenTileLayer("terrain");
   map.addLayer(layer); // Optional

   //Code to convert TopoJson to GeoJson
   L.TopoJSON = L.GeoJSON.extend({ 
                  addData: function(jsonData) {   
                           if (jsonData.type === "Topology") {
                               for (key in jsonData.objects) {
                                    geojson = topojson.feature(jsonData, jsonData.objects[key]);
                                    L.GeoJSON.prototype.addData.call(this, geojson);
    }}   
                           else {
                                    L.GeoJSON.prototype.addData.call(this, jsonData);
    }}});
 
  topoLayer = new L.TopoJSON();
    // Possible Colour Schemes

  // Imports boundary data and passes to the addTopoData function
    mapLookup = d3.map();


d3.json(map_data_url, function (data) {
    console.log(data);
    data.dataset.forEach( function(d) {
    	mapLookup.set(d.areaname,d.cases_rate);   //+d.excess
    	});
    $.getJSON(shape_url).done(addTopoData);
    
});
};

// Colours used (uses parameters defined at start)

  function getColor(d) {
    return d == null ? 'white': 
           d > legend5 ? colourmatrix[colour_scheme][5] :
           d > legend4 ? colourmatrix[colour_scheme][4] :
           d > legend3 ? colourmatrix[colour_scheme][3] :
           d > legend2 ? colourmatrix[colour_scheme][2] :
           d > legend1 ? colourmatrix[colour_scheme][1] :
           d > legend0 ? colourmatrix[colour_scheme][0] :
                         'grey';
  }
  // Draws the boundary data on the map
function addTopoData(topoData) { 
           topoLayer.addData(topoData);
           topoLayer.addTo(map);
           topoLayer.eachLayer(handleLayer);
           zoom2place(startplace);
           
   }
 
 
// Set the style of the boundary data layer (fill color based on data values)
function handleLayer(layer) {
   //console.log(mapLookup.get(layer.feature.properties.lad16nm));
   layer_value=mapLookup.get(layer.feature.properties.areaname);
   layer.setStyle({ fillColor : getColor(layer_value),
                     fillOpacity: 0.6,
                     color: 'black',
                     weight:0.5,
                     opacity: 1 });
                    
   layer.on({ mouseover : enterLayer,
               mouseout: leaveLayer,
               click: clicklayer,  });
   
   layers[layer._leaflet_id] = layer;
   references[layer.feature.properties.areaname]=layer;
  } //End of handleLayer function

function zoom2place(place) {
    console.log('zooming to : '+place);
    
    try {
    map.fitBounds(references[place]._bounds)
    }
     catch(err) {
    console.log(err);
    };
   };

function loadData(src) {

    d3.json(src, function(error, data) {
        if (error) return console.warn(error);

        layers = {}; // reset reference

        L.geoJSON(data, {
            style: myStyle,
            onEachFeature: eachFeature
        }).addTo(map);

    });
}

   function zoomToFeature(e) {
        console.log(e)
        var feature = L.geoJson(e).addTo(map);
		map.fitBounds(feature.getBounds());
        //map.fitBounds(e.getBounds());
//        country = e.target.feature.properties.name;		// To update the select
//            $("#state").val(country);
        }


  // Add Tooltip feature
  var info = L.control();
 
  info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
  };
 
  // Behaviour when mouseover an area
  function enterLayer(){  
       this.setStyle({ weight: 2, opacity: 1 });
       var areaname = this.feature.properties.areaname; // Local Authority Name
       var areaid = this.feature.properties.areacode;   // LA code 
       var excess=mapLookup.get(areaname)
       // method that we will use to update the tooltip feature
       info.update = function () {
         if (display_value=='cases_rate')
            {
            this._div.innerHTML = stat_name + ' <br/> <b>' + areaname + '</b> <br/> '+ excess+ ' cases per 100,000 people';
         }else
        	{
        this._div.innerHTML = stat_name + ' <br/> <b>' + areaname + '</b> <br/> '+ excess+ ' deaths per 100,000 people';
        };
    };
        info.addTo(map); 
  };

  function clicklayer(){
      clickplace= this.feature.properties.areaname;
      console.log('clicked on '+clickplace);
      //zoomToFeature(this.feature);
      get_data(clickplace);
  };


  // Behaviour when mouseout an area
  function leaveLayer(){
       this.setStyle({ weight: 0.5 });
       // method that we will use to reset the tooltip feature
       info.update = function () {
            this._div.innerHTML = 'Hover over an area for more information';
       };
       info.addTo(map);
  }; 

