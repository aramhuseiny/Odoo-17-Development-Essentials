/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { evaluateBooleanExpr } from "@web/core/py_js/py";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

import { useService } from '@web/core/utils/hooks';
import { Component, onWillStart, useState } from "@odoo/owl";

const formatters = registry.category("formatters");

export class CbadgeField extends Component {
    static template = "library.CbadgeField";
    static props = {
        ...standardFieldProps,
        decorations: { type: Object, optional: true },
    };
    static defaultProps = {
        decorations: {},
    };

    setup() {
        super.setup();
        this.orm = useService('orm');

        this.state = useState({
            categories: {}
        });

        onWillStart(async () => {
            const expense_states = await this.orm.call("library.category", 'get_expense_dashboard', []);
            console.log("after orm call")
            this.state.categories = expense_states;
            console.log(this.state.categories);
        });
    }
    get formattedValue() {
        const formatter = formatters.get(this.props.record.fields[this.props.name].type);
        return formatter(this.props.record.data[this.props.name], {
            selection: this.props.record.fields[this.props.name].selection,
        });
    }

    get classFromDecoration() {
        const evalContext = this.props.record.evalContextWithVirtualIds;
        for (const decorationName in this.props.decorations) {
            if (evaluateBooleanExpr(this.props.decorations[decorationName], evalContext)) {
                return `text-bg-${decorationName}`;
            }
        }
        return "";
    }

    consoleState() {
        console.log(this.state.categories);
    } 
}

export const cbadgeField = {
    component: CbadgeField,
    displayName: _t("Badge"),
    supportedTypes: ["selection", "many2one", "char"],
    extractProps: ({ decorations }) => {
        return { decorations };
    },
};
console.log("hi there")
registry.category("fields").add("cbadge", cbadgeField);
