class Fix():

	def fixDict_(self, query):
		tam=0
		ID = 0
		json_res={}
		json={}
		lista=[]
		
		
		response=[]
		activitiesList=[]
		report={}
		activity={}
		self.query=query
		for obj in self.query:
			if ID == obj["reporte_id"]:
				activity = {}
					
				activity.update({"ActRealizada_id":obj["ActRealizada_id"]})
				activity.update({"ActRealizada_observaciones":obj["ActRealizada_observaciones"]})
				activity.update({"realizado":obj["realizado"]})
				activity.update({"accesorio_id":obj["accesorio_id"]})
				activity.update({"actividades_id":obj["actividades_id"]})
				activity.update({"actividad_id":obj["actividad_id"]})
				activity.update({"actividad_nombre":obj["actividad_nombre"]})
				activity.update({"accesorio_nombre":obj["accesorio_nombre"]})
				activity.update({"ActAlert_id":obj["ActAlert_id"]})
				activity.update({"foco_id":obj["foco_id"]})
				activity.update({"colorFoco":obj["colores"]})
				activity.update({"descripcionFoco":obj["descripcion"]})
				
				response[len(response)-1]['actividadesRealizadas'].append(activity)
				
			else:
				
				report = {}
				
				ID = query[tam]["reporte_id"]
				report['reporte_id'] = obj["reporte_id"]
				report['creado_por'] = obj["creado_por"]
				report['reporte_observaciones'] = obj["reporte_observaciones"]
				report['inicio'] = obj["inicio"]
				report['fin'] = obj["fin"]
				report['cuarto_id'] = obj["cuarto_id"]
				report['cuarto_nombre'] = obj["cuarto_nombre"]
				report['piso_nombre'] = obj["piso_nombre"]
				
				activity = {}
				activitiesList = []
					
				activity.update({"ActRealizada_id":obj["ActRealizada_id"]})
				activity.update({"ActRealizada_observaciones":obj["ActRealizada_observaciones"]})
				activity.update({"realizado":obj["realizado"]})
				activity.update({"accesorio_id":obj["accesorio_id"]})
				activity.update({"actividades_id":obj["actividades_id"]})
				activity.update({"actividad_id":obj["actividad_id"]})
				activity.update({"actividad_nombre":obj["actividad_nombre"]})
				activity.update({"accesorio_nombre":obj["accesorio_nombre"]})
				activity.update({"ActAlert_id":obj["ActAlert_id"]})
				activity.update({"foco_id":obj["foco_id"]})
				activity.update({"colorFoco":obj["colores"]})
				activity.update({"descripcionFoco":obj["descripcion"]})
				
				
				'''
				activity.update({"reporte_id":obj["reporte_id"]})
				activity.update({"creado_por":obj["creado_por"]})
				activity.update({"reporte_observaciones":obj["reporte_observaciones"]})
				activity.update({"inicio":obj["inicio"]})
				activity.update({"fin":obj["fin"]})
				activity.update({"cuarto_id":obj["cuarto_id"]})
				activity.update({"cuarto_nombre":obj["cuarto_nombre"]})
				activity.update({"piso_nombre":obj["piso_nombre"]})
				
				'''
				
				activitiesList.append(activity)
				
				report.update({"actividadesRealizadas":activitiesList})
				
				
				response.append(report)
				
			tam = tam + 1
		
		return response

