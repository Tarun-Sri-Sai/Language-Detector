import { NgModule } from '@angular/core'
import { BrowserModule } from '@angular/platform-browser'
import { FormsModule } from '@angular/forms'
import { HttpClientModule } from '@angular/common/http'

import { AppComponent } from './app.component';
import { TitleComponent } from './title/title.component';
import { InputComponent } from './input/input.component';
import { ResultComponent } from './result/result.component'

@NgModule({
  declarations: [
    AppComponent,
    TitleComponent,
    InputComponent,
    ResultComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
