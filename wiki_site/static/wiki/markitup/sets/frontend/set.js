// -------------------------------------------------------------------
// markItUp!
// -------------------------------------------------------------------
// Copyright (C) 2008 Jay Salvat
// http://markitup.jaysalvat.com/
// -------------------------------------------------------------------
// MarkDown tags example
// http://en.wikipedia.org/wiki/Markdown
// http://daringfireball.net/projects/markdown/
// -------------------------------------------------------------------
// Feel free to add more tags
// -------------------------------------------------------------------
mySettings = {
	previewParserPath:	'',
	onShiftEnter:		{keepDefault:false, openWith:'\n\n'},
	// kjh
	markupSet: [
		// {name:'First Level Heading', key:'1', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '=') } },
		// {name:'Second Level Heading', key:'2', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '-') } },
		{name:'First Level Heading', key:'1', openWith:'# ', placeHolder:'Your 1st title here...' },
		{name:'Second Level Heading', key:'2', openWith:'## ', placeHolder:'Your 2nd title here...' },
		{name:'Heading 3', key:'3', openWith:'### ', placeHolder:'Your 3rd title here...' },
		{name:'Heading 4', key:'4', openWith:'#### ', placeHolder:'Your 4th title here...' },
		{name:'Heading 5', key:'5', openWith:'##### ', placeHolder:'Your 5th title here...' },
		{name:'Heading 6', key:'6', openWith:'###### ', placeHolder:'Your 6th title here...' },
		{separator:'---------------' },
		{name:'Bold', key:'B', openWith:'**', closeWith:'**'},
		{name:'Italic', key:'I', openWith:'_', closeWith:'_'},
		{separator:'---------------' },
		{name:'Bulleted List', openWith:'- ' },
		{name:'Numeric List', openWith:function(markItUp) {
			return markItUp.line+'. ';
		}},
		{separator:'---------------'},
		{name:'Quotes', openWith:'> '},
		// {name:'Code Block / Code', openWith:'(!(    |!|`)!)', closeWith:'(!(`)!)'},
		{name:'Code Block / Code', openWith:'```\n', placeHolder:'Your code here', closeWith:'\n``` '},
	]
}

// mIu nameSpace to avoid conflict.
miu = {
	markdownTitle: function(markItUp, char) {
		heading = '';
		n = $.trim(markItUp.selection||markItUp.placeHolder).length;
		for(i = 0; i < n; i++) {
			heading += char;
		}
		return '\n'+heading;
	}
}
