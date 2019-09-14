"""Example of simple query to SOAP service"""
import suds.client

client = suds.client.Client('http://api-tt.belavia.by/TimeTable/Service.asmx?WSDL')
result = client.service.GetAirportsList('EN')
print(result)

client = suds.client.Client('http://api-tt.belavia.by/TimeTable/Service.asmx?WSDL')
result = client.service.GetTimeTable('SVO', 'Arrival', '2019-09-14')
print(result)