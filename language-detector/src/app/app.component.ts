import { Component } from '@angular/core'
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  textInput: string = ''
  result: string = ''

  constructor(private http: HttpClient) { }

  detectLanguage(): void {
    if (!this.isValidLength()) {
      return
    }

    this.http.get<any>(`http://localhost:5000/detect-language?input_text=${this.textInput}`)
      .subscribe({
        next: (response) => {
          this.result = `This text is in ${response.language_code}`
        },
        error: (error) => {
          console.error('Error occurred during language detection:', error)
        }
      })
  }

  isValidLength(): boolean {
    return this.textInput.trim().replaceAll(/\s+/g, ' ').length >= 10
  }
}