# form di input per activity sheet
<h6 class="quicksand"><b>Scheda manutenzione preventiva</b></h6>
<fieldset><legend>Dati intervento</legend>
! $ 1 entry_date 2 entry_time 2
! $ 1 component 3 $ 1 requested_by 2
! $ 1 status 2
# ! $ 1 description 10
</fieldset>
<br/>

<fieldset><legend>Personale interno Uniacque</legend>
! $ 1 internal_responsible 3 $ 1 num_internal_operators 1
! $ 1 internal_intervention_time_days 1 internal_intervention_time_hours 1 internal_intervention_time_minutes 1
! $ 1 internal_intervention_duration  1
</fieldset>
<br/>

<fieldset><legend>Personale esterno Uniacque</legend>
! $ 1 external_company 2
! $ 1 external_responsible 3 $ 1 num_external_operators 1
! $ 1 external_intervention_time_days 1 external_intervention_time_hours 1 external_intervention_time_minutes 1
! $ 1 external_intervention_duration 1
</fieldset>
<br/>

<fieldset><legend>Consuntivo intervento</legend>
! $ 1 intervention_start_date 2 $ 1 intervention_start_time 2
! $ 1 intervention_completion_date 2 $ 1 intervention_completion_time 2
! $ 1 machine_down_time_days 1 machine_down_time_hours 1 machine_down_time_minutes 1
! $ 1 machine_down_time_duration 1

    <div id="preventiva">
    <fieldset><legend>Manutenzione preventiva</legend>
! $ 1 intervention_type 3 $ 1 component_status 3
! $ 1 intervention_description 6
    </fieldset>
    </div>

    <div id="correttiva">
    <fieldset><legend>Manutenzione correttiva</legend>
! $ 1 fault_type  4
! $ 1 fault_cause  4
! $ 1 fault_effect  4
! $ 1 fault_description 6
! $ 1 intervention_description 6
    </fieldset>
    </div>

    <div id="ispettiva">
    <fieldset><legend>Manutenzione ispettiva</legend>
! $ 1 intervention_description 6
! $ 1 measurements 6
    </fieldset>
    </div>

</fieldset>



