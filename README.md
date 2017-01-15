# mallcloud
MallCloud DeepLibrary Models

1. Frontend creates json file and sends it to the mallcloud servers.
<br>json example:
  ```
  {
      "parameters" : {
           "mallcloudid" : "productid",
           "transactionid" : "our_transactionid",
           "lineitemnumber" : "itemnumber"
       },
       
       "templates" : {
           "M_Helmets" : { "DEFAULT" },
           "M_Helmets_F" : { "DEFAULT" },
           "Nxt_Thrty_Days" : { "CUSTOM" },
           "Lng_Time_No_See" : { "DISABLE" }
       },
       
       "Nxt_Thrty_Days" : {
           "Algorithms" : ['NeuralNet', 'RidgeRegression', 'SVM', 'RandomForest'],
           "Parameters" : ['productid', 'itemnumber']
       }
  }
  ```
> Parameters refer to mapping between names of columns in internal system vs user's system.
Users can let the templates stay enabled or disable certain templates according to their needs.
User can either use default system which chooses the algorithms and parameters for them 
or Customize the system and use different algorithms and/or parameters used.

2. After the mallcloud servers get the json file, they break it down into pieces according to Templates needed.
The format is converted to the tensorflow supported ProtocolBuffer system. The templates are created by taking
algorithm definitions from models available, parameter list and algorithm list from ProtocolBuffer defined for 
that particular template(ProtocolBuffers are extracted from JSON provided by user as mentioned).

3. The system computes templates and provides json based interaction between templates and the user.

4. After all templates are done internally ie, each template has created predictions using multiple algorithms and 
superlearner has chosen the best prediction values, the results are sent to the Deep Neural Network.

5. Deep Neural Network will provide final results. Results of all templates can be extracted by user upon demand using 
the JSON api from `point 3`. This JSON api also provides graphs in order to observe the templates' 
results and each algorithm's results from a particular template.
User is allowed to tweak almost everything in the system or just use the default values.

6. Proper logging and error api has been created to provide instructions and help get back to a working system.
