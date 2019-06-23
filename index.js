var bodyParser = require("body-parser");
var path = require('path');
var express = require('express');
var url = require('url');
var spawn = require("child_process").spawn;
var cors = require("cors");
// var config = require('./config');
var MongoClient = require('mongodb').MongoClient;
var app = express();

app.set('port', (process.env.PORT || 5000));
app.use(express.static(__dirname + '/public'));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

var readStream = function(stream, res) {
  var output = '';
  stream.on('data', function(data) {
    output += data.toString()
  })
  stream.on('end', function() {
    res.send(output);
  })
}

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});

app.post('/getportfolio', async function(req, res) {
  console.log('/getportfolio api called')
  var process = await spawn('python',["./analyzer.py", 
                       "--config", 
                       JSON.stringify(req.body.params),
                       "--to_json"]);
  readStream(process.stdout, res)
});

app.get('/getfunds', async function(req, res) {
  console.log('/getfunds api requested')
  var process = await spawn('ls',["data"]);
  readStream(process.stdout, res)
  console.log(res)
});

// var db_url = config.url;

// app.get('/new/*', function (req, res) {
  
//   // var URL = req.Url.path;
//   var path_name = (req.path)
//   if(path_name.length<=5){
//     res.send({error:"you are gonna need some valid url after /new/"})
//   }
//   path_name=path_name.substring(5,path_name.length);
//   console.log(path_name);
//   console.log('IsURL: ', config.isURL(path_name) );
//   var link=url.parse(path_name);
//   console.log(link);
  
//   if( config.isURL(path_name) ){
//     var info={};
//     var hash = (link.hostname==null?'':link.hostname) + (link.pathname==null || link=='/'?'':link.pathname);
//     console.log(hash);
//     info.original_url=path_name;
//     info.short_url=req.headers['host']+'/';
    
//     console.log(req.headers['host']);
    
//     var latest_doc;
//     var query_fun = function (query_type) {
//       MongoClient.connect(db_url, 
//         function (err, db) {
//           if (err) {
//             throw new Error("Unable to connect to the mongoDB server")
//           } else {
//             console.log('Connection established to', db_url);
            
//               var collection=db.collection('url_table');
              
//               if(query_type=='findOne'){
//                 collection.findOne({ original_url:hash} , function(err, doc) {
//                         console.log('inside findOne function');
//                         if(err){
//                             throw new Error("Unable to query the mongoDB server")
//                         }else{
//                             console.log('doc',doc);
//                             if(doc==null){
//                               latest_doc={_id:shortid.generate(),original_url:hash};
//                               console.log()
//                               console.log('latest_doc=',latest_doc);
//                               info.short_url+=latest_doc._id;
//                               query_fun('insert');
//                             }else{
//                               info.short_url+=doc._id;
//                             }
//                             res.send(info);
//                         }
//                     }
//                 );
//               }else{
//                 console.log('?q',latest_doc);
//                 collection.insert( latest_doc , function(error, data) {
//                     console.log('data',data);
//                     if (error) throw error;
//                     console.log('url',hash,'addded successfully');
//                 }); 
//               }
              
//           }
//           db.close();
//         }
//       );
//       console.log('out of here !!!',query_type,latest_doc);
//     }
    
//     query_fun('findOne');
    
//   }else{
//     var info;
//     console.error('Invalid url');
//     info.error='Invalid url address given in query';
//     res.send(info);
//   }
// });


// app.get('/:ID', function (req, res) {
  
//   var info={};
//   var id=req.params.ID;
//   console.log('requested new request',id);
//   if( !shortid.isValid(id) ){
//     info.error='This url does not exist in database';
//     res.send(info);
//     return ;
//   }

//   MongoClient.connect(db_url, 
//     function (err, db) {
//       if (err) {
//         throw new Error("Unable to connect to the mongoDB server")
//       } else {
//         console.log('Connection established to', db_url);
        
//           var collection=db.collection('url_table');
          
//           collection.findOne({ _id:id} , function(err, doc) {
//                   if(err){
//                       throw new Error("Unable to query the mongoDB server")
//                   }else{
//                       console.log(doc);
//                       if(doc==null){
//                         info.error='this url does not exist in database';
//                         res.send(info)
//                         db.close();
//                       }else{
//                         db.close();
//                         console.log( 'old address ',doc.original_url);
//                         res.redirect('http://'+doc.original_url);
//                       }
//                   }
//               }
//           );
//       }
//     }
//   );
  
// });

