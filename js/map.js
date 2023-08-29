//隐藏单位选择
document.getElementById("select_units").style.display = "none";
// 创建一个比例尺控件
var scaleLineControl = new ol.control.ScaleLine({
  units: "metric",
  // 比例尺默认的单位
});
var grid=0;
//实例化OSM图层数据源对象
var osmSource = new ol.source.OSM();
//加载瓦片网格图层
var gridLayer = new ol.layer.Tile({
  //瓦片网格数据源
  source: new ol.source.TileDebug({
    //投影
    projection: 'EPSG:3857',
    //获取瓦片网格信息
    tileGrid: osmSource.getTileGrid()
  })
})
//底图图层
//var url = 'https://gac-geo.googlecnapps.cn/maps/vt?lyrs=s&x={x}&y={y}&z={z}';
var r_layer = new ol.layer.Tile({
  source: new ol.source.XYZ({
    url: 'https://gac-geo.googlecnapps.cn/maps/vt?lyrs=s&x={x}&y={y}&z={z}',
    wrapX: false,
  }),
});
//加载瓦片网格图层
var gridLayer = new ol.layer.Tile({
  //瓦片网格数据源
  source: new ol.source.TileDebug({
    //投影
    projection: 'EPSG:3857',
    //获取瓦片网格信息
    tileGrid: osmSource.getTileGrid()
  })
})

// var geoLayer = new ol.layer.Vector({
//   source: new ol.source.Vector({
//       format: new ol.format.GeoJSON(),
//       url:'/data/bj.geojson'
//   })
// });

var view = new ol.View({
  projection: "EPSG:4326",
  center: [104, 34],
  zoom: 4,
  extent: [-180, -85, 180, 85],
})
let map = new ol.Map({
  target: "map",
  controls: ol.control.defaults().extend([
    scaleLineControl,
    // 将比例尺控件添加到地图中
  ]),

  layers: [r_layer],
  view: view
});
//设置底图url
function setUrl(url) {
  //alert(url);
  //url = url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}";
  r_layer.getSource().setUrl(url)
  //刷新地图
  map.getLayers().forEach(layer => layer.getSource().refresh());
  map.addLayer(geoLayer)
}
//监听鼠标左键信号
map.on("singleclick", (evt) => {
  console.log(evt.coordinate);
  //sendMes(evt.coordinate[0], evt.coordinate[1]);
});
//右键
$(map.getViewport()).on("contextmenu", function (event) {
  event.preventDefault(); //屏蔽自带的右键事件
  map.removeInteraction(draw);
  console.log("1111");
});
window.onload = function () {
  new QWebChannel(qt.webChannelTransport, function (channel) {
    window.printer = channel.objects.printer; // 此处channel.objects.printer中的printer就是上文提到的功能类注册的标识名
  });
};

//绘制矩形
function draw_jx() {
  //map.addLayer(layer);
  source.clear();
  map.addInteraction(draw);
}
var unitsSelect = document.getElementById("units");
// 让地图的比例尺单位根据用户的选择而改变
unitsSelect.addEventListener(
  "change",
  function () {
    scaleLineControl.setUnits(unitsSelect.value);
  },
  false
);
// 监听层级变化，输出当前层级和分辨率
map.getView().on("change:resolution", function () {
  document.getElementById("zoom").innerHTML =
    this.getZoom().toFixed(0) + " ";
});

document.getElementById("zoom").innerHTML =
  map.getView().getZoom().toFixed(0) + " ";

function gridView() {
  //alert('grid=',grid)
  if (grid==0) {
    map.addLayer(gridLayer)
    grid=1
  }
  else {
    map.removeLayer(gridLayer)
    grid=0
  }

}