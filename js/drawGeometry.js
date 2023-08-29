//import { getBottomLeft, getBottomRight, getTopLeft, getTopRight } from '../ol7/extent';
//创建源及图层
var source = new ol.source.Vector();
var v_layer = new ol.layer.Vector({
    source: source
})
v_layer.set('name','vLayer')
map.addLayer(v_layer);

//画点功能
// var draw = new ol.interaction.Draw({
//     type: 'Point',
//     source: source,
//     free: false
// })
//矩形
draw = new ol.interaction.Draw({
    source: source,
    type: 'Circle',
    freehand: false,  
    geometryFunction: ol.interaction.Draw.createBox()
})
//map.addInteraction(draw);

draw.on('drawend', function(e) {
    source.clear();
    var geom = e.feature.getGeometry();//拿到绘制图形的geometry
    //map.removeInteraction(draw);//移除绘制状态，一次只绘制一个图形						
    //let featureGeoJson = JSON.parse(new GeoJSON().writeFeature(e.feature));//将绘制图层转为geojson
    console.log(geom.getCoordinates());
    console.log(geom.getExtent());
    console.log(geom.getExtent()[0]);
    
    sendMes(geom.getExtent()[0],geom.getExtent()[1],geom.getExtent()[2],geom.getExtent()[3],geom.getExtent()[4])
    
})
function sendMes(x1,y1,x2,y2) {
    // 调用python端的功能类的方法执行操作
    printer.setExtent(x1,y1,x2,y2);
  }



