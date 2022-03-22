# -*- coding: utf-8 -*-
# @Date    : 2020-06-02 21:54:08
# @Author  : fh
# @File    : py_Html.py
import  os
titles='接口测试报告'
def title(titles):
    title='''<!DOCTYPE html>
<html>
<head>
	<title>%s</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 引入 Bootstrap -->
    <link href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
    <script src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!--[if lt IE 9]>
     <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
     <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <style type="text/css">
        .hidden-detail,.hidden-tr{
            display:none;
        }
    </style>
</head>
<body>
	'''%(titles)
    return title
connent='''
<div  class='col-md-4 col-md-offset-4' style='margin-left:3%;'>
<h1>用例执行结果</h1>'''
def shouye(starttime,endtime,passge,fail,excepthions):
    msg='''
    <table  class="table table-hover table-condensed">
            <tbody>
                <tr>
		<td><strong>开始时间:</strong> %s</td>
		</tr>
		<td><strong>结束时间:</strong> %s</td></tr>
		<td><strong>耗时:</strong> %s</td></tr>
		<td><strong>结果:</strong>
			<span >成功: <strong >%s</strong>
			       失败: <strong >%s</strong>
			       异常: <strong >%s</strong>                  
			   </tr> 
			   </tbody></table>
			   </div> '''%(starttime,endtime,(endtime-starttime),passge,fail,excepthions)
    return msg
detail='''<div class="row " style="margin:60px">
        <div style='    margin-top: 18%;' >
        <div class="btn-group" role="group" aria-label="...">
            <button type="button" id="check-all" class="btn btn-primary">所有用例</button>
            <button type="button" id="check-success" class="btn btn-success">成功用例</button>
            <button type="button" id="check-warning" class="btn btn-warning">失败用例</button>
            <button type="button" id="check-orther" class="btn check-orther">错误用例</button>           
        </div>
        <div class="btn-group" role="group" aria-label="...">
        </div>
        <table class="table table-hover table-condensed table-bordered" style="word-wrap:break-word; word-break:break-all;  margin-top: 7px;">
		<tr>
            <td nowrap="nowrap" align="center"><strong>ID</strong></td>
            <td nowrap="nowrap" align="center"><strong>名称</strong></td>
            <td nowrap="nowrap" align="center"><strong>URL</strong></td>
            <td nowrap="nowrap" align="center"><strong>请求方式</strong></td>
            <td nowrap="nowrap" align="center"><strong>预期</strong></td>
            <td nowrap="nowrap" align="center"><strong>返回内容</strong></td>
            <td nowrap="nowrap" align="center"><strong>结果</strong></td>
        </tr>
    '''
def passfail(tend):
    if tend =='pass':
        htl='''<td bgcolor="green" nowrap="nowrap">PASS</td>'''
    elif tend =='fail':
        htl='''<td bgcolor="fail" nowrap="nowrap">FAIL</td>'''
    else:
        htl = '<td bgcolor="crimson" nowrap="nowrap">ERROR</td>'
    return htl
def test_detail(reslt,id,name,url,method,expect,response_datas,result):
    detail_msg='''
        <tr class="case-tr %s">
            <td align="center" nowrap="nowrap">%s</td>
            <td nowrap="nowrap">%s</td>
            <td nowrap="nowrap">%s</td>
            <td align="center" nowrap="nowrap">%s</td>
            <td>%s</td>
            <td>%s</td>
            %s
        </tr>
    '''%(reslt,id,name,url,method,expect,response_datas,passfail(result))
    return detail_msg
weibu='''</div></div></table>
<script type="text/javascript">
	$("#check-warning").click(function(e){
		 $(".case-tr").removeClass("hidden-tr");
        $(".success").addClass("hidden-tr");
        $(".error").addClass("hidden-tr");
	});
	$("#check-success").click(function(e){
		 $(".case-tr").removeClass("hidden-tr");
        $(".warning").addClass("hidden-tr");
        $(".error").addClass("hidden-tr");
	});
	$("#check-orther").click(function(e){
		 $(".case-tr").removeClass("hidden-tr");
        $(".warning").addClass("hidden-tr");
        $(".success").addClass("hidden-tr");
	});
	$("#check-all").click(function(e){
	    $(".case-tr").removeClass("hidden-tr");
	});
</script>
</body></html>'''
def result_msg(result):
    relus=' '
    for i in result:
        if i['result'] == "pass":
            clazz = "success"
        elif i['result'] == "fail":
            clazz = "warning"
        else:
            clazz = "error"
        relus+=test_detail(clazz,int(i['id']),i['name'],i['url'],i['method'].upper(),i['expect'],i['realdata'],i['result'])
    return relus
def fullhtml(titles,starttime,endtime,passcount,failcount,errorcount,relus):        
    text=title(titles)+connent+shouye(starttime,endtime,passcount,failcount,errorcount)+detail+relus+weibu
    return text

def createhtml(report_html,filepath):
    with open(filepath,'wb') as f:
        f.write(report_html.encode('utf-8'))