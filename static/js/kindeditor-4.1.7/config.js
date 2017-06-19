KindEditor.ready(function(K) {
               K.create("#id_content",{
                   width : '1000px',
                   height : '300px',
                   uploadJson: '/admin/upload/kindeditor',
                   items : [
						'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
						'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
						'insertunorderedlist', '|', 'emoticons', 'image', 'link']
               });
        });