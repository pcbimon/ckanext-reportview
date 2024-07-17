from __future__ import annotations
from typing import Any, cast

from ckan.common import CKANConfig
from ckan.lib.plugins import DefaultTranslation
from ckan.types import Context, DataDict, Schema
import ckan.plugins as p
import ckan.plugins.toolkit as tk
import logging
log = logging.getLogger(__name__)


# import ckanext.reportview.cli as cli
# import ckanext.reportview.helpers as helpers
# import ckanext.reportview.views as views
# from ckanext.reportview.logic import (
#     action, auth, validators
# )
ignore_empty = p.toolkit.get_validator("ignore_empty")
class ReportviewPlugin(p.SingletonPlugin, tk.DefaultDatasetForm,DefaultTranslation):
    p.implements(p.ITranslation)
    p.implements(p.IConfigurer)
    p.implements(p.IDatasetForm)
    p.implements(p.IResourceView, inherit=True)
    def _modify_package_schema(self, schema: Schema) -> Schema:
        # Add our resource_report_id_text metadata field to the schema
        cast(Schema, schema['resources']).update({
                'resource_report_id_text' : [ tk.get_validator('ignore_missing') ]
                })
        return schema

    def create_package_schema(self):
        schema: Schema = super(
            ReportviewPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema: Schema = super(
            ReportviewPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
    def show_package_schema(self) -> Schema:
        schema: Schema = super(
            ReportviewPlugin, self).show_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self) -> list[str]:
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
    # IConfigurer

    def update_config(self, config: CKANConfig):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
    # IResourceView
    def info(self)-> dict[str, Any]:
        return {
            "name": "report_view",
            "title": p.toolkit._("Dashboard View"),
            "icon": "tachometer",
            "schema": {"report_id": [ignore_empty]},
            "iframed": True,
            "always_available": True,
            "default_title": p.toolkit._("report_view"),
        }
    def can_view(self, data_dict:DataDict) -> bool:
        resource = data_dict.get('resource')
        report_id = ''
        if resource:
            report_id = resource.get('resource_report_id_text')
            # check if report_id is not empty
            if report_id == '':
                return False
            return True
        return False
    def view_template(self, context: Context, data_dict: DataDict) -> str:
        return 'report_iframe.html'
    def setup_template_variables(self, context: Context,
                                 data_dict: DataDict) -> dict[str, Any]:
        config = tk.config
        base_url = config.get('ckanext.reportview.baseurl', 'https://default-reportapp-url')
        # add query params to the base url key reportId
        base_url = base_url + '?reportId='          
        resource = data_dict.get('resource')
        report_id = ''
        if resource:
            report_id = resource.get('resource_report_id_text')
        base_url = base_url + report_id
        return {
            'report_url': base_url,
        }
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    
