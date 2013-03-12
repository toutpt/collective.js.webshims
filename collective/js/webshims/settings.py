import json
from zope import component
from zope import schema
from zope import interface
from collective.js.webshims import i18n
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.schema.vocabulary import SimpleVocabulary


features_vocabulary = SimpleVocabulary.fromValues([
    'json-storage',
    'es5',
    'geolocation',
    'canvas',
    'forms',
    'forms-ext',
    'mediaelement',
    'track',
    'details',
])


class PolyfillOptions(interface.Interface):
    """options of jquery polyfill
    http://afarkas.github.com/webshim/demos/index.html#polyfill-options
    """
    debug = schema.Bool(title=u"Debug mode", default=False)

    features = schema.List(
       title=u"Features",
       required=False,
       value_type=schema.Choice(title=u"Feature",
                                vocabulary=features_vocabulary),
    )
    wait_ready = schema.Bool(title=u"Wait for ready", default=True)
    extendNative = schema.Bool(title=u"Wait for ready", default=True)

    # basePath is computed by the viewlet to use this addon

    disableShivMethods = schema.Bool(title=u"Disable shiv methods",
                                     default=True)


class FormsOptions(interface.Interface):
    """Options for 'form' feature"""

    customMessages = schema.Bool(title=i18n.customMessages,
                                 description=i18n.customMessages_desc,
                                 default=False)

    replaceValidationUI = schema.Bool(title=i18n.replaceValidationUI,
                                 description=i18n.replaceValidationUI_desc,
                                 default=False)

    placeholderType = schema.ASCIILine(title=i18n.placeholderType,
                                 description=i18n.placeholderType_desc,
                                 default="value")

    lightweightDatalist = schema.Bool(title=i18n.lightweightDatalist,
                                 description=i18n.lightweightDatalist_desc,
                                 default=True)

    customDatalist = schema.Bool(title=i18n.customDatalist,
                                 description=i18n.customDatalist_desc,
                                 default=False)

    positionDatalist = schema.Bool(title=i18n.positionDatalist,
                                 description=i18n.positionDatalist_desc,
                                 default=False)


class FormsExtOptions(interface.Interface):
    """Options for 'forms-ext' feature"""

    replaceUI = schema.Bool(title=i18n.replaceUI,
                            description=i18n.replaceUI_desc,
                            default=False)


class SettingsViewlet(ViewletBase):
    """Settings viewlet"""

    def update(self):
        super(ViewletBase, self).update()
        registry = component.getUtility(IRegistry)
        formsOptions = registry.forInterface(FormsOptions, check=False)
        formsExtOptions = registry.forInterface(FormsExtOptions, check=False)

        self.js_webshimsFormsOptions = self.recordsToJSon(FormsOptions,
                                                          formsOptions)
        self.js_webshimsFormsExtOptions = self.recordsToJSon(FormsExtOptions,
                                                             formsExtOptions)
        self.js_webshimsOptions = '{"waitReady": false}'

    def recordsToJSon(self, rschema, records):
        fields = schema.getFields(rschema)
        configuration = {}
        for field_name in fields:
            configuration[field_name] = fields[field_name].default
        if records:
            for field_name in fields:
                value = getattr(records, field_name, None)
                if value is not None and value != configuration[field_name]:
                    configuration[field_name] = value
        return json.dumps(configuration)
