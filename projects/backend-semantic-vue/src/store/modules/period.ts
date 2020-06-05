import store from '@/store';
import {
    VuexModule,
    Module,
    getModule,
    Mutation,
    Action
} from 'vuex-module-decorators';
import { getCurrentPeriod } from '@/api/api';
import { CurrentPeriod } from '@/api/interface';

@Module({ dynamic: true, name: 'period', store })
class PeriodModule extends VuexModule {
    currentPeriod: CurrentPeriod | any = null;
    
    get getCurrent() { return this.currentPeriod };

    @Mutation
    SET_CURRENT_PERIOD(payload: CurrentPeriod | any) {
        this.currentPeriod = payload;
    }
    

    @Action({rawError: true})
    async initStates() {
        const data = await getCurrentPeriod();
        this.SET_CURRENT_PERIOD(data);
    }
}

export default getModule(PeriodModule);
