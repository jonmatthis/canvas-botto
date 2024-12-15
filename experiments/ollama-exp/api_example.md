
in one terminal
```sh
ollama serve
```

wherever else
```sh
jkl@jkls-MacBook-Air ~ % curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt":"Write a paragraph."
}'
```

```json
{"model":"llama3.2","created_at":"2024-12-13T19:05:50.737414Z","response":"The","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:50.766733Z","response":" old","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:50.797558Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:50.82555Z","response":" c","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:50.854748Z","response":"reak","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:50.88414Z","response":"y","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:50.913113Z","response":" door","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:50.941958Z","response":" swung","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:50.971369Z","response":" open","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.001016Z","response":" with","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.029788Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.058062Z","response":" gentle","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.088088Z","response":" sc","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.11706Z","response":"ree","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.147174Z","response":"ch","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.175561Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.205055Z","response":" revealing","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.233728Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.26285Z","response":" world","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.291426Z","response":" that","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.321007Z","response":" was","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.349744Z","response":" frozen","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.379584Z","response":" in","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.409063Z","response":" time","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.438752Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.46787Z","response":" The","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.497926Z","response":" air","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.526181Z","response":" inside","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.555261Z","response":" was","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.584408Z","response":" stale","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.614644Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.64354Z","response":" must","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.672405Z","response":"y","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.700523Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.729012Z","response":" carrying","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.757533Z","response":" the","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.787319Z","response":" scent","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.81662Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.845756Z","response":" forgotten","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.873988Z","response":" memories","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.903575Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.932552Z","response":" aged","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.962738Z","response":" dust","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:51.991302Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.021069Z","response":" As","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.049521Z","response":" I","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.078989Z","response":" stepped","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.108106Z","response":" across","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.137533Z","response":" the","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.166542Z","response":" threshold","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.195517Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.223812Z","response":" my","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.253228Z","response":" eyes","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.28212Z","response":" adjusted","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.311351Z","response":" to","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.34072Z","response":" the","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.369324Z","response":" dim","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.398459Z","response":" light","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.427148Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.456644Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.486701Z","response":" I","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.51504Z","response":" saw","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.543923Z","response":" it","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.572895Z","response":" -","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.602178Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.630881Z","response":" room","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.660311Z","response":" filled","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.68893Z","response":" with","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.718265Z","response":" the","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.746952Z","response":" remnants","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.77676Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.805939Z","response":" lives","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.835243Z","response":" long","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.863492Z","response":" past","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.892987Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.922026Z","response":" Old","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.951296Z","response":" furniture","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:52.980004Z","response":" stood","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.009126Z","response":" like","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.037566Z","response":" sent","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.066451Z","response":"in","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.094997Z","response":"els","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.125156Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.154172Z","response":" their","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.184064Z","response":" surfaces","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.21246Z","response":" worn","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.241586Z","response":" smooth","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.27038Z","response":" by","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.299768Z","response":" the","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.328192Z","response":" touch","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.357493Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.386994Z","response":" countless","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.416172Z","response":" hands","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.444722Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.473507Z","response":" In","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.502991Z","response":" the","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.531665Z","response":" center","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.55972Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.589706Z","response":" the","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.61878Z","response":" room","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.6482Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.677338Z","response":" a","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.706156Z","response":" grand","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.734985Z","response":" piano","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.763929Z","response":" sat","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.792408Z","response":" upright","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.822264Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.851012Z","response":" its","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.880419Z","response":" keys","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.909376Z","response":" yellow","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.939896Z","response":"ed","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.968691Z","response":" with","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:53.998209Z","response":" age","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.026127Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.054998Z","response":" yet","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.084051Z","response":" still","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.11413Z","response":" radi","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.142958Z","response":"ating","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.171967Z","response":" an","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.200641Z","response":" aura","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.230156Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.258616Z","response":" promise","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.288977Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.3182Z","response":" possibility","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.34728Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.375944Z","response":" It","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.405536Z","response":" was","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.435067Z","response":" as","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.465286Z","response":" if","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.49423Z","response":" time","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.523194Z","response":" had","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.552367Z","response":" paused","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.581864Z","response":" here","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.611558Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.640837Z","response":" leaving","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.670113Z","response":" behind","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.699848Z","response":" only","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.728598Z","response":" echoes","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.758217Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.78807Z","response":" laughter","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.817477Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.846725Z","response":" tears","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.87622Z","response":",","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.905584Z","response":" whispers","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.935056Z","response":" of","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.96397Z","response":" love","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:54.99392Z","response":" and","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:55.022251Z","response":" loss","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:55.052073Z","response":".","done":false}
{"model":"llama3.2","created_at":"2024-12-13T19:05:55.08108Z","response":"","done":true,"done_reason":"stop","context":[128006,9125,128007,271,38766,1303,33025,2696,25,6790,220,2366,18,271,128009,128006,882,128007,271,8144,264,14646,13,128009,128006,78191,128007,271,791,2362,11,272,1127,88,6134,70955,1825,449,264,22443,1156,770,331,11,31720,264,1917,430,574,20268,304,892,13,578,3805,4871,574,51451,323,2011,88,11,15691,279,41466,315,25565,19459,323,20330,16174,13,1666,358,25319,4028,279,12447,11,856,6548,24257,311,279,5213,3177,11,323,358,5602,433,482,264,3130,10409,449,279,73440,315,6439,1317,3347,13,10846,14891,14980,1093,3288,258,2053,11,872,27529,24634,11113,555,279,5916,315,28701,6206,13,763,279,4219,315,279,3130,11,264,6800,27374,7731,49685,11,1202,7039,14071,291,449,4325,11,3686,2103,12164,1113,459,40142,315,11471,323,13336,13,1102,574,439,422,892,1047,35595,1618,11,9564,4920,1193,71057,315,43214,323,24014,11,89248,315,3021,323,4814,13],"total_duration":4555714458,"load_duration":19173542,"prompt_eval_count":29,"prompt_eval_duration":191000000,"eval_count":150,"eval_duration":4344000000}
```