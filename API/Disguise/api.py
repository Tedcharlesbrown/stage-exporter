endpoints = [
   {
      "path":"api/session/status/health",
      "description":"List all health status for the machines in the network",
      "returns":{
         "status":{
            "code":"int",
            "message":"string",
            "details":[
               {
                  "type_url":"string",
                  "value":"string"
               }
            ]
         },
         "result":[
            {
               "machine":{
                  "uid":"string",
                  "name":"string",
                  "hostname":"string"
               },
               "runningAsMachine":{
                  "uid":"string",
                  "name":"string",
                  "hostname":"string"
               },
               "status":{
                  "averageFPS":"int",
                  "videoDroppedFrames":"int",
                  "videoMissedFrames":"int",
                  "states":[
                     {
                        "name":"string",
                        "detail":"string",
                        "category":"string",
                        "severity":"string"
                     }
                  ]
               }
            }
         ]
      }
   },
   {
      "path":"api/session/status/project",
      "description":"Return the project information",
      "returns":{
        "status": {
            "code": "int",
            "message": "string",
            "details": [
            {
                "type_url": "string",
                "value": "string"
            }
            ]
        },
        "result": {
            "projectPath": "string",
            "version": {
            "major": "int",
            "minor": "int",
            "hotfix": "int",
            "revision": "int"
            }
        }
      }
   }
]