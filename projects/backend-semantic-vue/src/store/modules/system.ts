import store from '@/store';
import {
    VuexModule,
    Module,
    getModule,
    Mutation,
    Action
} from 'vuex-module-decorators';
import { getSystems, getDefects } from '@/api/api';
import { System } from '@/api/interface';

@Module({ dynamic: true, name: 'system', store })
class SystemModule extends VuexModule {
    currentSystemList: System[] | any = null;

    get currentSystems() { return this.currentSystemList; }

    @Mutation
    SET_CURRENT_SYSTEM_LIST(payload: System[] | any) {
        this.currentSystemList = payload;
    }

    @Action
    async initStates() {
        const data = await getSystems();
        const systems = [];
        for(const system of data) {
            const defects = await getDefects(system.id)
            system.defects = defects;
            systems.push(system);
        }
        this.SET_CURRENT_SYSTEM_LIST(systems);
    }
}

export default getModule(SystemModule);