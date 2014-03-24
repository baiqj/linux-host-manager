var cloudAppFileControllers = angular.module('cloudAppFileControllers', []);

cloudAppFileControllers.controller('FileCtrl',['$scope','$http',
    function($scope,$http){

        //$('#_xsrf').val(getCookie('XSRF-TOKEN'));
        var hasChange = false;
        var editor = CodeMirror(document.getElementById('editor'), {
            value: '',
            lineNumbers: true,
            lineWrapping: true,
            matchBrackets: true,
            onCursorActivity: function() {
                editor.setLineClass(hlLine, null, null);
                hlLine = editor.setLineClass(editor.getCursor().line, null, 'activeline');
                // disable match highlight in IE, or it will slow down the page
                if (!$.support.msie) editor.matchHighlight('CodeMirror-matchhighlight');
            },
            onChange: function() {
                hasChange = true;
            }
        });
        var hlLine = editor.setLineClass(0, 'activeline');

        var filedata = {
            "mimetype": "text/x-java",
            "content": "import java.text.SimpleDateFormat;\nimport java.text.ParseException;\nimport java.util.Date;\nimport java.util.TimeZone;\nclass time{\n    public static void main(String[] args) throws ParseException {\n        SimpleDateFormat sf = new SimpleDateFormat(\"yyyy-MM-dd HH:mm:ss\");\n        sf.setTimeZone(TimeZone.getTimeZone(\"Asia/shanghai\"));\n        String str3 = \"1927-12-31 23:54:07\";\n        String str4 = \"1927-12-31 23:54:08\";\n        Date sDt3 = sf.parse(str3);\n        Date sDt4 = sf.parse(str4);\n        long ld3 = sDt3.getTime() /1000;\n        long ld4 = sDt4.getTime() /1000;\n        System.out.println(ld3);\n        System.out.println(ld4);\n        System.out.println(ld4-ld3);\n    }\n}\n//for test file edit function and get params",
            "charset": "utf-8",
            "filename": "1.java",
            "filepath": "/root/1.java"
        };

        $scope.currentDir = '/root/pythonPro';

        $scope.entryDir = function(dirName){
            if(dirName == ''){
                $scope.currentDir = '/root';
            } else {
                $scope.currentDir = $scope.currentDir + '/' + dirName;
            }
            console.log('Current DIR is:' + $scope.currentDir);
            $scope.listdir($scope.currentDir);
        }
        $scope.listdir = function(currentDir){
            console.log('[lsitdir]Current DIR is:' + $scope.currentDir);
            $http({method: 'POST',
                url: '/operation/file',
                data:{
                    'action':'listdir',
                    'path': currentDir,
                    'showhidden': false,
                    'remember': false}
            }).
            success(function(data, status, headers, config){
                console.log('Get the data:' + data);
                if(data.code == 0){
                    $scope.items = data.data;
                    console.log("Get /root info success.");
                } else {
                    console.log('Get /root info failed.');
                }
            }).
            error(function(data,status,headers,config){
                    console.log('failed get "/root" dir lists!');
            });
        }

        $scope.readfile =function(filename){
            var path = $scope.currentDir + '/' + filename;
            $http({method:'POST',
                url:'/operation/file',
                data:{
                    'action':'fread',
                    'path': path,
                    'remember':false
                }}).
                success(function(data,status,headers,config){
                    console.log(data);
                    if(data.code == 0){
                        var filedata = data.data;

                        $scope.filename = filedata.filename;
                        $scope.filepath = filedata.filepath;
                        $scope.filecharset = filedata.charset;
                        $scope.filecharset_org = filedata.charset;
                        editor.setValue('');
                        $('#edit').show();
                        $('#dirlist').hide();
                        editor.setOption('mode', filedata.mimetype);
                        editor.setValue(filedata.content);
                        hasChange = false;

                    }
                    else{
                        console.log('Get file content failed');
                    }
                }).
                error(function(data,status,headers,config){
                    console.log("send request for getting file contents failed");
                });
        }

        $scope.saveFile = function(){
            console.log($scope.filepath);
            $http({method:'POST',
                url:'/operation/file',
                data:{
                    'action': 'fwrite',
                    'path': $scope.filepath,
                    'charset': $scope.filecharset,
                    'content': editor.getValue()
                }
            }).
                success(function(data,status,headers,config){
                    console.log(data);
                }).
                error(function(data,status,headers,config){
                    console.log('send save file request failed');
                });
        }
        $scope.newFile = function(fileName){

        }
        $scope.back = function(){
            $http({
                method: 'POST',
                url:    '/operation/file',
                data:{
                    'action':  'fclose'
                }
            }).
            success(function(data,status,headers,config){
                    console.log(data);
                    if(data.code == 0){
                        console.log("文件被关闭。");
                        $('#edit').hide();
                        $('#dirlist').show();
                    }
                    else{
                        console.log('文件关闭失败～～');
                    }
                }).
            error(function(data,status,headers,config){
                console.log('发送文件关闭请求失败～～');
            });
        }

        $scope.upandlist = function(){
             var patharr = $scope.currentDir.split('/');
             patharr.pop();
             $scope.currentDir = patharr.join('/');
             console.log('[upandlist]Current Dir is:',$scope.currentDir);
             $scope.listdir(patharr.join('/')+'/');
         }

        $scope.newfolder = function(){
            console.log('[newfoler] Function newfolder() has been called!!');
            $('#newfolder').modal();
            $http({
                    method: 'POST',
                    url:    'operation/file',
                    data:{
                        'action':'createfolder',
                        'path':$scope.currentDir,
                        'name':$scope.newfolderName
                    }
            }).
            success(function(data,status,headers,config){
                    console.log(data);
                    $scope.listdir($scope.currentDir);
            }).
            error(function(data,status,headers,config){

            });
        }

        $scope.newfile = function(){
            console.log('[newfile] Function newfile() has been called!!');
            $('#newfile').modal();
            $http({
                method: 'POST',
                url:    'operation/file',
                data:{
                    'action':'createfile',
                    'path':$scope.currentDir,
                    'name':$scope.newfileName
                }
            }).
                success(function(data,status,headers,config){
                    console.log(data);
                    $scope.listdir($scope.currentDir);
                }).
                error(function(data,status,headers,config){

                });
        }

        $scope.uploadfile = function(){
            console.log('[uploadfile] Function uploadfile() has been called!!');
            $('#uploadfile').modal();

            console.log('[uploadfile] Function uploadfile() has been called!!');
        }

        $scope.douploadfile = function(){
            $('#uploadform').submit();
        }

        $scope.rename = function(oldname){
            $('#newname').modal();
            $scope.newname = function(){
                $http({
                        method:'POST',
                        url:    'operation/file',
                        data:{
                                'action':'rename',
                                'path': $scope.currentDir + '/' + oldname,
                                'name': $scope.newfileName
                        }
                }).
                success(function(data,status,header,config){
                        console.log(data);

                }).
                error(function(data,status,header,config){
                        console.log('Rename failed!!!!!!');
                });

            };
        }

        $scope.move2trash = function(name){
            $http({
                    method:'POST',
                    url:    '/operation/file',
                    data:   {
                            'action':'delete',
                            'paths':  $scope.currentDir + '/' + name
                    }
            }).
            success(function(data,status,header,config){
                    console.log(data);
                    if (data.code == 0) {
                        $scope.listdir($scope.currentDir);
                        //$scope.getitem(name);
                        // deal with .filename.bak
                        var bakname = '.'+name+'.bak';
                        /*for (var i=0;i<$scope.items.length;i++) {
                            if ($scope.items[i].name == bakname) {
                                $scope.getitem(bakname);
                                break;
                            }
                        }*/
                    }
                }).
            error(function(data,status,header,config){
                    console.log(data);
                });

        }
    }

])