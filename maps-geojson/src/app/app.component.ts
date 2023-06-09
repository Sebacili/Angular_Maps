@ViewChild('mapRef') mapRef!: GoogleMap;
ngAfterViewInit() {
  this.mapRef.data.addGeoJson(this.geoJsonObject);
}
  this.mapRef.data.setStyle(this.styleFunc)
}
styleFunc = (feature:any) =>{
  console.log(feature.h.id)
  let newColor = "#FF0000"; //RED
  if(feature.h.id == 0) newColor = "#00FF00"; //GREEN
  else newColor = "#0000FF"; //BLUE
  return ({
    clickable: false,
    fillColor: newColor,
    strokeWeight: 1
  });
}

markerGenerator() {
  this.markerList =[
    {
      position : {
        lng : this.geoJsonObject.features[0].geometry.coordinates[0][0][0],
        lat : this.geoJsonObject.features[0].geometry.coordinates[0][0][1]
      },
      label: String(this.geoJsonObject.features[0].properties.id),
    },
    {
      position : {
        lng : this.geoJsonObject.features[1].geometry.coordinates[0][0][0],
        lat : this.geoJsonObject.features[1].geometry.coordinates[0][0][1]
      },
      label: String(this.geoJsonObject.features[1].properties.id),
    },
  ]
    //Questi dati dovremmo scaricarli dal server, per ora li abbiamo copiati nel file     gojson.model.ts
    this.geoJsonObject = GEOJSON;  
    console.log(this.geoJsonObject); //stampo l'oggetto geoJsonObject sulla console
    this.markerGenerator();
  }

  @ViewChild('mapRef') mapRef!: GoogleMap;
}
}