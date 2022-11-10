const templateArgs = {
    mainUrl: '',
    paras: {templateId: ''}
}
const template_category = [];
const template_info = {
    cdn_prefix: '',
    templates: [],
    name: ''
};

$(function () {

    $("#template_input").keyup(function () {
        templateArgs.paras.templateId = $(this).val();
        set_main_url();
    });
    call_studio_api();
});

function set_main_url() {
    let main_url = templateArgs.mainUrl;
    let para = ''
    $.each(templateArgs.paras, function (key, value) {

        if (value !== '') { // value가 빈 값이 아니면 고고
            para += key + '=' + value + '&'; // 더해질 때마다 and가 들어가면 되는데, 여기서 넣고 마지막에 빼주도록 한다.
        }

    });

    //마지막 문자 가져오기
    //console.log(str.charAt(str.length-1));
    //마지막 문자 자르기
    //console.log(str.slice(0,-1));
    //마지막 문자 자르기
    //console.log(str.substr(0, str.length -1));

    para = para.substring(0, para.length - 1); // 마지막에 &요소 지워준다.
    main_url += para; // main url에다가 parameter을 더해준다.
    $("#scheme_input").val(main_url);
}

function call_studio_api() {

    $.ajax({
        url: "../ajax/api/studio",
        success: function (result) {
            // 통신이 성공적으로 이루어졌을 때 이 함수를 타게 된다.  TO-DO
            var category_html = ''
            for (var i = 0; i < result.result.categories.length; i++) {
                const template_id = result.result.categories[i].templateIds;
                const title = result.result.categories[i].title;
                template_category.push({'templateIds': template_id, 'title': title})
                category_html += `<div class="template-category">${title}</div>`
            }
            $(".studioCategoryRow").append(category_html);


            template_info.cdn_prefix = result.result.cdnPrefix;

            for (var i = 0; i < result.result.templates.length; i++) {
                const template_id = result.result.templates[i].id;
                const thumbnail = result.result.templates[i].thumbnail;
                const name = result.result.templates[i].name;
                template_info.templates.push({'id': template_id, 'thumbnail': thumbnail, 'name': name})
            }

            $(".template-category").click(function () {
                var title = $(this).text();
                var filter_temp = template_category.filter(e => e.title === title);
                var current_template = []
                for (var i = 0; i < filter_temp[0].templateIds.length; i++) {
                    current_template.push(template_info.templates.filter(e => e.id === filter_temp[0].templateIds[i])[0])
                }
                let sub_html = ''
                current_template.forEach(function (value, index, array) {

                    var thumb = template_info.cdn_prefix + 'template/' + value.id + '/' + value.thumbnail;
                    sub_html += `<div class="studio_block"><div>${value.id}</div>
                        <img src="${thumb}"></img>                        
                        <div>${value.name}</div>
                        </div>`;

                })
                const html = `
            <div className="contentsListContainer">
               
                  <div class="studio_group"> 
                    ${sub_html}
                    </div>
            </div>`
                $(".content-main").append(html);
            });

// image thumbnail 가운데 오도록 함,
// https://wiki.navercorp.com/pages/viewpage.action?pageId=586662251
// API Category List : 전체 카테고리 리스트를 내려준다.
//filter.id, filter.name, filter.thumbnail 값을 읽어와서 화면에 출력하면 된다.
//Thumbnail Url은: result.cdnPrefix + filter.thumbnail 로 사용한다.
//filter.thumbnail 이 없는 케이스도 있으니 예외 처리가 필요하다.


// console.log(sub_html)
// 자바스크립트에서 중괄호는 객체를 의미 , $ajax{}도 마찬가지이다.
// style category를 group으로 나눈다.

// 위에서 j까지 만들어 지고, 여기서부터 더해진다.
// id, name이 보이게 한다.
//


        },
        error: function (e) {
            console.error(e);
        }
    })
}