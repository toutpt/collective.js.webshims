from zope import i18nmessageid
_ = i18nmessageid.MessageFactory('collective.js.webshims')

customMessages = _(u"customMessages")
customMessages_desc = _(u"If customMessages is set to true. Webshims Lib will"\
    u"implement a DOM-Property called customValidationMessage, which can be"\
    u"changed through the $.webshims.validityMessages-Array."
)

replaceValidationUI = _(u"replaceValidationUI")
replaceValidationUI_desc = _(u"Replaces the browser validation UI with a"\
    u"custom styleable UI."
)
placeholderType = _(u"placeholderType")
placeholderType_desc = _(u"If placeholderType is set to 'over', the polyfill"\
    u"uses the overLabel technique to create a placeholder and doesn't"\
    u"'pollute' the value property."
)
lightweightDatalist = _(u"lightweightDatalist")
lightweightDatalist_desc = _(u"If lightweightDatalist is set to true."\
    u"Webshims Lib will switch the datalist element and list property"\
    u"implementation from the forms-ext to the forms feature."
)
customDatalist = _(u"customDatalist")
customDatalist_desc = _(u"Allows to use custom styleable datalist elements in"\
    u"all browsers."
)
positionDatalist = _(u"positionDatalist")
positionDatalist_desc = _(u"If positionDatalist is true or the input element"\
    u"has the class 'position-datalist', the datalist shim element is added"\
    u"right after the input elementand not appended to the body"\
    u"(good for :hover menus)."
)

replaceUI = _(u"replaceUI")
replaceUI_desc = _(u"If replaceUI is set to true the date and slider Widgets"\
    u"are replaced in all browsers (also in browser, which have implemented"\
    u"these types). This is useful, if you want to style the UI in all"
    u"browsers."
)
