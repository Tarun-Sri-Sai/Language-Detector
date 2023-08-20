import { Component } from '@angular/core';
import { LanguageService } from '../language.service';

@Component({
    selector: 'app-result',
    templateUrl: './result.component.html',
    styleUrls: ['./result.component.css'],
})
export class ResultComponent {
    constructor(public languageService: LanguageService) {}
}
