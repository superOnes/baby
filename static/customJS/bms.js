//编辑账户
// 获取内容
function editUser(userID){
  var editOrderUser = $("#editOrderUser");
  $.ajax({
    type:'post',
    url:'/admin/back/',
    async:true,
    data:{id:userID},
    success:function(results){
      var data = results.data;
        editOrderUser.find("input[name='username']").val(data.username);
        editOrderUser.find("input[name='name']").val(data.name);
        editOrderUser.find("input[name='house_limit']").val(data.house_limit);
        editOrderUser.find("input[name='expire_date']").val(data.expire_date);
        editUserCity()
        editUserCity(data.province);
        setTimeout(function(){
          $("#provinceE option[value='"+data.province+"']").attr("selected","selected");
          $("#downtownE option[value='"+data.city+"']").attr("selected","selected");
        },100);
    },
    error:function(){
      new $.zui.Messager("编辑获取信息失败", {
        placement:'center',
        type: 'danger'
      }).show()
    }
  })
};
// 编辑提交
function editSubmit(userID){
  var editOrderUser = $("#editOrderUser");
  var username = editOrderUser.find("input[name='username']").val();
  var name = editOrderUser.find("input[name='name']").val();
  var password = editOrderUser.find("input[name='password']").val();
  var house_limit = editOrderUser.find("input[name='house_limit']").val();
  var province = editOrderUser.find("#provinceE").val();
  var downtown = editOrderUser.find("#downtownE").val();
  if(username=="" || name=="" || password=="" || house_limit=="" || province==0 || downtown==0){
      new $.zui.Messager("请填写必填项", {
        placement:'center',
        type: 'danger'
      }).show()
  }else{
    var form = new FormData(document.getElementById("editOrderUser"));
    form.append('id',userID)
    $.ajax({
        url:"/admin/modify/",
        type:"post",
        data:form,
        processData:false,
        contentType:false,
        success:function(data){
          if(data.success){
            new $.zui.Messager('保存成功！', {
              placement:'center',
              type: 'success'
            }).show("",function(){
              setTimeout(function(){
                window.location.reload();
              },1000)
            });
          }else {
            new $.zui.Messager(data.msg, {
              placement:'center',
              type: 'danger'
            }).show()
          }
        },
        error:function(e){
          new $.zui.Messager("保存失败，请检查网络！", {
            placement:'center',
            type: 'danger'
          }).show()
        }
    });
  }
}

// 创建提交
function test(){
  var createOrderUser = $("#createModal");
  var username = createOrderUser.find("input[name='username']").val();
  var name = createOrderUser.find("input[name='name']").val();
  var password = createOrderUser.find("input[name='password']").val();
  var house_limit = createOrderUser.find("input[name='house_limit']").val();
  var province = $("#provinceC").val();
  var downtown = $("#downtownC").val();
  var passPatt = /^[a-zA-Z0-9]{6,10}$/;
  if(username=="" || name=="" || password=="" || house_limit=="" || province==0 || downtown==0){
      new $.zui.Messager("请填写必填项", {
        placement:'center',
        type: 'danger'
      }).show()
  }else if(!passPatt.test(password)){
    new $.zui.Messager("请输入6-10位数字字母结合的密码", {
      placement:'center',
      type: 'danger'
    }).show();
    return false;
  }else {
    var form = new FormData(document.getElementById("customerOrder"));
    $.ajax({
        url:"/admin/createuser/",
        type:"post",
        data:form,
        processData:false,
        contentType:false,
        success:function(data){
          if(data.success){
            new $.zui.Messager('创建成功！', {
              placement:'center',
              type: 'success'
            }).show("",function(){
              setTimeout(function(){
                window.location.reload();
              },1000)
            });
          }else {
            new $.zui.Messager(data.msg, {
              placement:'center',
              type: 'danger'
            }).show()
          }
        },
        error:function(e){
          new $.zui.Messager("创建失败，请检查网络！", {
            placement:'center',
            type: 'danger'
          }).show()
        }
    });
  }
}

// 编辑用户获取地址
function editUserCity(provinceId){
  if(!provinceId){
    var urls = "/admin/getprovince/";
    var appendObj = $("#provinceE");
  }else {
    var urls = "/admin/getcity/";
    var appendObj = $("#downtownE");
  }
  $.ajax({
    type:"get",
    url:urls,
    async:true,
    data:{proid:provinceId},
    success:function(results){
      var data = results.data;
      if(results.success){
        appendObj.children(".city").remove();
        for(var i=0; i<data.length; i++){
          appendObj.append("<option class='city' value="+data[i].id+">"+data[i].name+"</option>")
        };
      }
    },
    error:function(){
      new $.zui.Messager('获取省份、市区数据失败，请检查网络！', {
        placement:'center',
        type: 'danger'
      }).show();
    }
  });
};

// 创建用户获取地址
function createUser(provinceId){
  if(!provinceId){
    var urls = "/admin/getprovince/";
    var appendObj = $("#provinceC");
  }else {
    var urls = "/admin/getcity/";
    var appendObj = $("#downtownC");
  }
  $.ajax({
    type:"get",
    url:urls,
    async:true,
    data:{proid:provinceId},
    success:function(results){
      var data = results.data;
      if(results.success){
        appendObj.children(".city").remove();
        for(var i=0; i<data.length; i++){
          appendObj.append("<option class='city' value="+data[i].id+">"+data[i].name+"</option>")
        };
      }
    },
    error:function(){
      new $.zui.Messager('获取省份、市区数据失败，请检查网络！', {
        placement:'center',
        type: 'danger'
      }).show();
    }
  });
};

// 删除用户
function deleteUser(id){
  $.ajax({
    type:"post",
    url:"/admin/delete/",
    async:true,
    data:{id:id},
    success:function(data){
      if(data.success){
        window.location.reload();
      }else{
        new $.zui.Messager(data.msg, {
          placement:'center',
          type: 'danger'
        }).show();
      }
    },
    error:function(){
      alert("删除失败，请检查网络！");
    }
  });
}
// 密码重置
function resetUser(id){
  $.ajax({
    type:"put",
    url:"/admin/reset/",
    async:true,
    data:{id:id},
    success:function(data){
      if(data.success){
        new $.zui.Messager("密码重置成功！", {
          placement:'center',
          type: 'danger'
        }).show("",function(){
          setTimeout(function(){
            window.location.reload();
          },1000)
        });
      }else{
        new $.zui.Messager(data.msg, {
          placement:'center',
          type: 'danger'
        }).show();
      }
    },
    error:function(){
      alert("重置密码失败，请检查网络！");
    }
  });
};

// 退出
function loginOutYes(){
  $.ajax({
    type:'post',
    url:'/admin/logout/',
    async:true,
    success:function(){
        window.location.reload();
    },
    error:function(){
      alert("退出失败，请检查网络！")
    }
  })
}
